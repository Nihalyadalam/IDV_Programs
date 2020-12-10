import pandas as pd
import plotly.express as px

uniq_professor = []
uniq_lecture = []

f = pd.read_csv("DataWeierstrass.csv", ';')
data_frame = pd.DataFrame(f)

img_scatter = px.scatter_matrix(f,
                                dimensions=['participants', 'professional expertise', 'motivation', 'clear presentation', 'overall impression'],
                                color='professor', symbol='lecture')
img_scatter.update_traces(diagonal_visible=False)
img_scatter.update_layout(title="ScatterPlot-Matrix", height=1200, width=1000)
img_scatter.show()

for line in range(0, len(data_frame)):
    uniq_professor.append(int(data_frame['professor'][line].replace('prof', '')))
    uniq_lecture.append(int(data_frame['lecture'][line].replace('lecture', '')))

prof_data_col = pd.DataFrame({'professor': uniq_professor})
lecture_data_col = pd.DataFrame({'lecture': uniq_lecture})
data_frame.update(prof_data_col)
data_frame.update(lecture_data_col)

data_frame['professor'] = pd.to_numeric(data_frame['professor'])
data_frame['lecture'] = pd.to_numeric(data_frame['lecture'])


parallel_plot = px.parallel_coordinates(data_frame,
                dimensions=['professor', 'lecture', 'participants', 'professional expertise', 'motivation',
                                    'clear presentation', 'overall impression'], color='motivation')
parallel_plot.update_layout(title="Parallel-plot")
parallel_plot.show()


