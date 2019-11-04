class Report():
    def func(self):
        return 'Report'


class HTTPReport(Report):
    def func(self):
        return 'Http Report'

class TCPReport(Report):
    def func(self):
        return 'Tcp Report'


class Adapter():
    def adapt(self, arg):
        print(arg.func())

class HTMLAdapter(Adapter):
    pass


class TcpAdapter(HTMLAdapter):
    def adapt(self, tcpAdapter):
        if type(tcpAdapter) != TcpAdapter:
            raise ChildProcessError("guqjgfvqghev")
        else:
            print('error')

class HttpAdapter(HTMLAdapter):
    def adapt(self, arg):
        print("HTTP" + arg.func())


http_report = HTTPReport()
tcp_adapt = TcpAdapter()
tcp_adapt.adapt(http_report)