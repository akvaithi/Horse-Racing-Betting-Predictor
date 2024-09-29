import csv
import http.server
import socketserver
import cgi
import pandas as pd
from io import BytesIO
import json
from tensorflow.keras.models import load_model

# Load the model and make predictions
model = load_model('horseWinPredictor.h5')

class MyHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_OPTIONS(self):
        # Handle preflight requests for CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/predict':  # Ensure this matches the request URL
            try:
                # Parse the 'multipart/form-data' request
                ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
                if ctype == 'multipart/form-data':
                    pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
                    pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
                    form_data = cgi.parse_multipart(self.rfile, pdict)
                    
                    # Get the uploaded file
                    file_item = form_data.get('file')[0]  # 'file' is the name attribute of the input

                    # Add CORS headers to the response
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()

                    
                    # Assuming the file_item is a CSV file, read it into a DataFrame
                    df = pd.read_csv(BytesIO(file_item))
                    predictions = model.predict(df)

                    # Convert predictions to a list
                    predictions_list = predictions.tolist()

                    # Create a response dictionary
                    response = {'predictions': predictions_list}

                    # Send the JSON response
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                else:
                    self.send_response(400)
                    self.end_headers()
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                print(f"Error processing POST request: {e}")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    PORT = 5001
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
