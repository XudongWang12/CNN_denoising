import tensorflow as tf

with tf.Graph().as_default():
    output_graph_def = tf.GraphDef()
    output_graph_path = 'YourModelName_9750.pb'
    #sess.graph.add_to_collection("input", mnist.test.images)
 
    with open(output_graph_path, "rb") as f:
        output_graph_def.ParseFromString(f.read())
        print(output_graph_def)  # 输出图的节点操作
        _ = tf.import_graph_def(output_graph_def, name="")
 
    with tf.Session() as sess:
        tf.global_variables_initializer()
        test = sess.graph.get_tensor_by_name("embeddings:0")
        print(test)
