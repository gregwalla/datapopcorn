from flask import Flask, render_template
from content_management import Content
import pygal

from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

#variables
TOPIC_DICT = Content()



@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)


@app.route('/map/')
def map():
    return render_template("folium_boundaries.html")


@app.route('/pygalexample/')
def pygalexample():
	try:
		graph = pygal.Line()
		graph.title = '% Change Coolness of programming languages over time.'
		graph.x_labels = ['2011','2012','2013','2014','2015','2016']
		graph.add('Python',  [15, 31, 89, 200, 356, 900])
		graph.add('Java',    [15, 45, 76, 80,  91,  95])
		graph.add('C++',     [5,  51, 54, 102, 150, 201])
		graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
		graph_data = graph.render_data_uri()
		return render_template("graphing.html", graph_data = graph_data)
	except Exception as e:
		return(str(e))

#bokeh
def make_plot():
    plot = figure(plot_height=300, sizing_mode='scale_width')

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2**v for v in x]

    plot.line(x, y, line_width=4)

    script, div = components(plot)
    return script, div

@app.route('/bokehexample/')
def show_dashboard():
    plots = []
    plots.append(make_plot())

    return render_template('bokehdashboard.html', plots=plots)

