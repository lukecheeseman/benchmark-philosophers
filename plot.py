import plotly.graph_objects as go
import sys, os, csv

# plot "time" against memory where each time stamp is a discrete event

def plot(infile, outfile):
    layout = go.Layout(
        title = 'average time taken to complete dining philosophers',
        xaxis = dict(
            title = 'cores',
            showgrid = False
        ),
        yaxis = dict (
            title = 'time taken (s)'
        ),
        hovermode='closest'
    )
    fig = go.Figure(layout=layout)
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")

        cores = []
        acquire_one = []
        acquire_all = []
        for row in reader:
          cores.append(int(row["cores"]))
          acquire_one.append(float(row["one"]))
          acquire_all.append(float(row["all"]))

        fig.add_trace(go.Scatter(
          x = cores,
          y = acquire_one,
          mode = 'lines',
          name = f'acquire one cown'
        ))

        fig.add_trace(go.Scatter(
          x = cores,
          y = acquire_all,
          mode = 'lines',
          name = f'acquire all cowns'
        ))

    fig.write_html(outfile)

if __name__ == "__main__":
    result_file = sys.argv[1]

    plot(result_file, "out.html")
