https://towardsdatascience.com/historical-stock-price-data-in-python-a0b6dc826836
python -m venv venv
dos2unix venv/Scripts/activate
source venv/Scripts/activate
pip install -r requirements.txt

import matplotlib.pyplot as plt
>>> import pandas as pd
>>> tickers = ['AAPL', 'MSFT', '^GSPC']
>>> start_date = '2010-01-01'
>>> end_date = '2016-12-31'
>>> panel_data = data.DataReader('INPX', 'yahoo', start_date, end_date)
>>> panel_data.head(9)
                High       Low      Open     Close  Volume  Adj Close
Date
2012-08-03  680400.0  680400.0  680400.0  680400.0     0.0   680400.0
2012-08-06  680400.0  680400.0  680400.0  680400.0     0.0   680400.0
2012-08-07  243000.0  243000.0  243000.0  243000.0     0.0   243000.0
2012-08-08  243000.0  243000.0  243000.0  243000.0     0.0   243000.0
2012-08-09  729000.0  729000.0  729000.0  729000.0     0.0   729000.0
2012-08-10  729000.0  729000.0  729000.0  729000.0     0.0   729000.0
2012-08-13  729000.0  729000.0  729000.0  729000.0     0.0   729000.0
2012-08-14  243000.0  243000.0  243000.0  243000.0     0.0   243000.0
2012-08-15  243000.0  243000.0  243000.0  243000.0     0.0   243000.0
>>>

Serving the plotted chart in Flask:
https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask

Generating image:
https://gitlab.com/snippets/1924163

from flask import render_template
import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@app.route("/mysuperplot", methods=["GET"])
def plotView():

    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(range(5), range(5), "ro-")
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("image.html", image=pngImageB64String)

# In the image.html jinja2 template use the following <img> to add the plot:
# <img src="{{ image }}"/>


Serving image in Flask
https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response

from flask import send_file

@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'ok.gif'
    else:
       filename = 'error.gif'
    return send_file(filename, mimetype='image/gif')
	
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
