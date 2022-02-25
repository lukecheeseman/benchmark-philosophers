import plotly.graph_objects as go
import sys, os, json

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
    with open(infile, 'r') as jsonfile:
        logfile = json.load(jsonfile)

        for acquire in logfile.keys():
            times = logfile[acquire]

            fig.add_trace(go.Scatter(
              x = list(range(len(times))),
              y = [ time for time in times ],
              mode = 'lines',
              name = f'acquire {acquire} cown(s)'
            ))

    fig.write_html(outfile)

if __name__ == "__main__":
    logfiles = sys.argv[1]

    plot(logfiles, "out.html")