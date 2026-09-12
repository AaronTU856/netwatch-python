import socket

from netwatch.ports import check_tcp_port


def test_open_tcp_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))
        server.listen(1)

        host, port = server.getsockname()

        result = check_tcp_port(host, port)

        assert result.host == host
        assert result.port == port
        assert result.open is True


def test_closed_tcp_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))

        host, port = server.getsockname()

    result = check_tcp_port(host, port)

    assert result.host == host
    assert result.port == port
    assert result.open is False
    
    