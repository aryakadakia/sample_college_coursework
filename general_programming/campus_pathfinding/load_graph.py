from vertex import Vertex

v_dictionary = {}


def load_graph(data_file):
    campus_loc = open(data_file, "r")

    for location in campus_loc:
        vertex_name = location.split("; ")
        v_value = vertex_name[2].split(", ")
        v_dictionary[vertex_name[0]] = Vertex(vertex_name[0], int(v_value[0]), int(v_value[1]))
    campus_loc.close()

    campus_loc = open(data_file, "r")

    for location in campus_loc:
        vertex_name = location.split("; ")
        adj_v = vertex_name[1].split(", ")
        for element in adj_v:
            v_dictionary[vertex_name[0]].adj_list.append(v_dictionary[element])
        campus_loc.close()
        return v_dictionary
