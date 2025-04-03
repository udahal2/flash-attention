from manim import *

class LLMExplanationScene(Scene):
    def construct(self):
        # Title
        title = Text("Simulating Large Language Models (LLM)", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Let's go through the components step by step
        self.predict_sample_repeat()
        self.inside_transformer()
        self.word_embeddings()
        self.unembedding_process()
        self.softmax_temperature()

        # Final pause to let the audience absorb the content
        self.wait(2)

    def predict_sample_repeat(self):
        """
        Simulate the "Predict, Sample, Repeat" process in LLMs.
        """
        predict_text = Text("Step 1: Predict Next Token", font_size=24).to_edge(LEFT)
        sample_text = Text("Step 2: Sample from Distribution", font_size=24).next_to(predict_text, DOWN)
        repeat_text = Text("Step 3: Repeat for Next Token", font_size=24).next_to(sample_text, DOWN)

        # Show prediction
        self.play(Write(predict_text))
        self.wait(1)

        # Show sampling
        self.play(Write(sample_text))
        self.wait(1)

        # Show repeat process
        self.play(Write(repeat_text))
        self.wait(1)

    def inside_transformer(self):
        """
        Visualizing the inner workings of a transformer.
        This will show attention mechanism and how the model processes input.
        """
        transformer_title = Text("Inside a Transformer", font_size=24).to_edge(UP)
        self.play(Write(transformer_title))

        # Create some sample input matrices (e.g., Query, Key, Value)
        query_matrix = Matrix([[1, 0], [0, 1]], h_buff=1.5)
        key_matrix = Matrix([[1, 1], [0, 1]], h_buff=1.5)
        value_matrix = Matrix([[1, 2], [3, 4]], h_buff=1.5)
        
        query_label = Text("Query", font_size=24).next_to(query_matrix, UP)
        key_label = Text("Key", font_size=24).next_to(key_matrix, UP)
        value_label = Text("Value", font_size=24).next_to(value_matrix, UP)

        matrices_group = VGroup(query_matrix, key_matrix, value_matrix).arrange(RIGHT, buff=1.5)
        labels_group = VGroup(query_label, key_label, value_label)

        self.play(Write(query_label), Write(key_label), Write(value_label))
        self.play(Write(query_matrix), Write(key_matrix), Write(value_matrix))
        self.wait(2)

        # Show attention score calculation
        attention_score_matrix = Matrix([[0.8, 0.2], [0.5, 0.5]], h_buff=1.5)
        attention_score_label = Text("Attention Scores", font_size=24).next_to(attention_score_matrix, UP)
        self.play(Write(attention_score_label), Write(attention_score_matrix))
        self.wait(2)

        # Show the output (weighted sum of values)
        output_matrix = Matrix([[2.6, 3.4], [2.0, 2.5]], h_buff=1.5)
        output_label = Text("Output", font_size=24).next_to(output_matrix, UP)
        self.play(Write(output_label), Write(output_matrix))
        self.wait(2)

    def word_embeddings(self):
        """
        Visualize the concept of word embeddings in LLMs.
        """
        embedding_title = Text("Word Embeddings", font_size=24).to_edge(UP)
        self.play(Write(embedding_title))

        # Create word embeddings (vectors)
        word_1 = Text("Word 1", font_size=24).shift(LEFT * 3)
        word_2 = Text("Word 2", font_size=24).shift(RIGHT * 3)
        
        vector_1 = Line(LEFT * 0.5, RIGHT * 2).shift(LEFT * 3)
        vector_2 = Line(LEFT * 0.5, RIGHT * 2).shift(RIGHT * 3)
        
        self.play(Write(word_1), Write(word_2))
        self.play(GrowArrow(vector_1), GrowArrow(vector_2))
        self.wait(1)

        # Show high-dimensional space analogy
        high_dim_text = Text("Embedding in High-Dimensional Space", font_size=20).shift(DOWN * 2)
        self.play(Write(high_dim_text))
        self.wait(2)

    def unembedding_process(self):
        """
        Visualizing the unembedding process, where embeddings are transformed back to tokens.
        """
        unembedding_title = Text("Unembedding Process", font_size=24).to_edge(UP)
        self.play(Write(unembedding_title))

        # Create a vector that gets transformed back to a token
        embedding_vector = Line(LEFT * 0.5, RIGHT * 2)
        embedding_text = Text("Embedding Vector", font_size=20).next_to(embedding_vector, DOWN)

        token = Text("Token", font_size=24).shift(DOWN * 2)

        self.play(GrowArrow(embedding_vector), Write(embedding_text))
        self.play(Transform(embedding_vector, token))
        self.wait(2)

    def softmax_temperature(self):
        """
        Visualizing softmax function and the effect of temperature on token selection.
        """
        softmax_title = Text("Softmax with Temperature", font_size=24).to_edge(UP)
        self.play(Write(softmax_title))

        # Create a distribution of scores (before softmax)
        scores = Matrix([[2.5, 1.0, 0.5]], h_buff=1.5)
        scores_label = Text("Scores", font_size=20).next_to(scores, UP)
        self.play(Write(scores_label), Write(scores))
        self.wait(1)

        # Show softmax with temperature adjustment
        softmax_text = Text("Softmax", font_size=20).next_to(scores, DOWN)
        self.play(Write(softmax_text))
        self.wait(1)

        # Show the effect of temperature (lower temperature -> sharper distribution)
        temperature_text = Text("Temperature Effect", font_size=20).shift(DOWN * 2)
        self.play(Write(temperature_text))
        self.wait(1)

