#!/usr/bin/env bash
set -o errexit -o nounset -o pipefail

mkdir --parents /etc/nftables.d
cat >/etc/nftables.d/web-port-forwarding.nft <<'HEREDOC'
destroy table inet web_port_forwarding
table inet web_port_forwarding {
    chain prerouting {
        type nat hook prerouting priority dstnat;
        jump port_redirects
    }
    chain output {
        type nat hook output priority dstnat;
        fib daddr type local jump port_redirects
    }
    chain port_redirects {
        tcp dport 80 redirect to :8080
        tcp dport 443 redirect to :8443
        udp dport 443 redirect to :8443
    }
}
HEREDOC

cat >/etc/systemd/system/web-port-forwarding.service <<'HEREDOC'
[Unit]
After=nftables.service

[Service]
Type=oneshot
ExecStart=nft --file=/etc/nftables.d/web-port-forwarding.nft

[Install]
WantedBy=multi-user.target
HEREDOC

systemctl enable web-port-forwarding.service
systemctl restart web-port-forwarding.service
