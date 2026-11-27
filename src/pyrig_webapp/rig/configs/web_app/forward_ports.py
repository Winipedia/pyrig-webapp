"""Generate the web app host port forwarding setup script."""

from typing import override

from pyrig.rig.configs.base.shell import ShellConfigFile
from pyrig_runtime.core.strings import snake_to_kebab_case

from pyrig_webapp.rig.tools.web_app.server import WebServer


class ForwardPortsConfigFile(ShellConfigFile):
    """Generate a script that persistently forwards the host web ports."""

    @override
    def script(self) -> str:
        """Return the nftables and systemd setup commands."""
        http_port = WebServer.I.http_port()
        http_host_port = WebServer.I.http_host_port()
        https_port = WebServer.I.https_port()
        https_host_port = WebServer.I.https_host_port()
        table_name = self.table_name()
        redirect_chain_name = self.redirect_chain_name()
        rules_filename = self.rules_filename()
        service_filename = self.service_filename()
        return f"""mkdir --parents /etc/nftables.d
cat >/etc/nftables.d/{rules_filename} <<'HEREDOC'
destroy table inet {table_name}
table inet {table_name} {{
    chain prerouting {{
        type nat hook prerouting priority dstnat;
        jump {redirect_chain_name}
    }}
    chain output {{
        type nat hook output priority dstnat;
        fib daddr type local jump {redirect_chain_name}
    }}
    chain {redirect_chain_name} {{
        tcp dport {http_port} redirect to :{http_host_port}
        tcp dport {https_port} redirect to :{https_host_port}
        udp dport {https_port} redirect to :{https_host_port}
    }}
}}
HEREDOC

cat >/etc/systemd/system/{service_filename} <<'HEREDOC'
[Unit]
After=nftables.service

[Service]
Type=oneshot
ExecStart=nft --file=/etc/nftables.d/{rules_filename}

[Install]
WantedBy=multi-user.target
HEREDOC

systemctl enable {service_filename}
systemctl restart {service_filename}
"""

    @override
    def stem(self) -> str:
        """Return the forwarding script filename stem."""
        return "forward-ports"

    def redirect_chain_name(self) -> str:
        """Return the shared nftables redirect chain name."""
        return "port_redirects"

    def rules_filename(self) -> str:
        """Return the nftables rules filename."""
        return f"{self.table_filename_stem()}.nft"

    def service_filename(self) -> str:
        """Return the systemd service filename."""
        return f"{self.table_filename_stem()}.service"

    def table_filename_stem(self) -> str:
        """Return the table name formatted for filenames."""
        return snake_to_kebab_case(self.table_name())

    def table_name(self) -> str:
        """Return the nftables table name."""
        return "web_port_forwarding"
