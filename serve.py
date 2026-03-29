import http.server, os, sys
port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=port, bind="")
