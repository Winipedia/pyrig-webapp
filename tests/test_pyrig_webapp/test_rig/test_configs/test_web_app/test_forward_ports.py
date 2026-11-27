"""Test module."""

from pyrig_webapp.rig.configs.web_app.forward_ports import ForwardPortsConfigFile


class TestForwardPortsConfigFile:
    """Test class."""

    def test_redirect_chain_name(self) -> None:
        """Test method."""
        assert ForwardPortsConfigFile.I.redirect_chain_name() == "port_redirects"

    def test_rules_filename(self) -> None:
        """Test method."""
        assert ForwardPortsConfigFile.I.rules_filename() == "web-port-forwarding.nft"

    def test_script(self) -> None:
        """Test method."""
        script = ForwardPortsConfigFile.I.script()
        assert "destroy table inet web_port_forwarding" in script
        assert "table inet web_port_forwarding {" in script
        assert "type nat hook prerouting priority dstnat;" in script
        assert "jump port_redirects" in script
        assert "type nat hook output priority dstnat;" in script
        assert "fib daddr type local jump port_redirects" in script
        assert "chain port_redirects {" in script
        assert "tcp dport 80 redirect to :8080" in script
        assert "tcp dport 443 redirect to :8443" in script
        assert "udp dport 443 redirect to :8443" in script
        assert "ExecStart=nft --file=/etc/nftables.d/web-port-forwarding.nft" in script
        assert "systemctl enable web-port-forwarding.service" in script
        assert "systemctl restart web-port-forwarding.service" in script

    def test_service_filename(self) -> None:
        """Test method."""
        assert (
            ForwardPortsConfigFile.I.service_filename() == "web-port-forwarding.service"
        )

    def test_stem(self) -> None:
        """Test method."""
        assert ForwardPortsConfigFile.I.stem() == "forward-ports"
        assert ForwardPortsConfigFile.I.path().as_posix() == "scripts/forward-ports.sh"

    def test_table_filename_stem(self) -> None:
        """Test method."""
        assert ForwardPortsConfigFile.I.table_filename_stem() == "web-port-forwarding"

    def test_table_name(self) -> None:
        """Test method."""
        assert ForwardPortsConfigFile.I.table_name() == "web_port_forwarding"
