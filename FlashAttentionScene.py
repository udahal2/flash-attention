from manim import *

class FlashAttentionScene(Scene):
    def construct(self):
        # Create the main title and animate it
        title = Text("Flash Attention Mechanism", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Create and display matrices: Query, Key, and Value
        query_matrix, key_matrix, value_matrix = self.create_matrices()

        # Create labels for each matrix
        query_label, key_label, value_label = self.create_labels(query_matrix, key_matrix, value_matrix)

        # Display the matrices and labels
        self.display_matrices_and_labels(query_label, key_label, value_label, query_matrix, key_matrix, value_matrix)

        # Introduce Attention Scores and animate
        attention_scores, attention_label = self.create_attention_scores()
        self.display_attention_scores(attention_label, attention_scores)

        # Introduce Output and animate
        output_matrix, output_label = self.create_output_matrix()
        self.display_output(output_label, output_matrix)

        # Draw arrows to explain how the flow works in attention mechanism
        self.add_arrows(query_matrix, key_matrix, attention_scores, output_matrix)

        # Final pause to let the audience absorb the content
        self.wait(2)

    def create_matrices(self):
        """
        Creates the matrices for Query, Key, and Value.

        Returns:
            tuple: Containing the query, key, and value matrices.
        """
        query_matrix = Matrix([[1, 0], [0, 1]], h_buff=1.5)
        key_matrix = Matrix([[1, 1], [0, 1]], h_buff=1.5)
        value_matrix = Matrix([[1, 2], [3, 4]], h_buff=1.5)
        
        return query_matrix, key_matrix, value_matrix

    def create_labels(self, query_matrix, key_matrix, value_matrix):
        """
        Creates labels for the Query, Key, and Value matrices.

        Returns:
            tuple: Containing the labels for query, key, and value.
        """
        query_label = Text("Query", font_size=24).next_to(query_matrix, UP)
        key_label = Text("Key", font_size=24).next_to(key_matrix, UP)
        value_label = Text("Value", font_size=24).next_to(value_matrix, UP)
        
        return query_label, key_label, value_label

    def display_matrices_and_labels(self, query_label, key_label, value_label, query_matrix, key_matrix, value_matrix):
        """
        Displays the Query, Key, and Value matrices with their respective labels.

        Args:
            query_label, key_label, value_label: The labels for the matrices.
            query_matrix, key_matrix, value_matrix: The matrices themselves.
        """
        matrices_group = VGroup(query_matrix, key_matrix, value_matrix).arrange(RIGHT, buff=1.5)
        labels_group = VGroup(query_label, key_label, value_label)

        self.play(Write(query_label), Write(key_label), Write(value_label))
        self.play(Write(query_matrix), Write(key_matrix), Write(value_matrix))
        self.wait(1)

    def create_attention_scores(self):
        """
        Creates the Attention Scores matrix.

        Returns:
            tuple: The Attention Scores matrix and its label.
        """
        attention_scores = Matrix([[0.8, 0.2], [0.5, 0.5]], h_buff=1.5)
        attention_label = Text("Attention Scores", font_size=24).next_to(attention_scores, UP)
        attention_scores.next_to(self.matrices_group, DOWN, buff=1.5)
        
        return attention_scores, attention_label

    def display_attention_scores(self, attention_label, attention_scores):
        """
        Displays the Attention Scores matrix along with its label.

        Args:
            attention_label: The label for the Attention Scores matrix.
            attention_scores: The Attention Scores matrix itself.
        """
        self.play(Write(attention_label), Write(attention_scores))
        self.wait(1)

    def create_output_matrix(self):
        """
        Creates the Output matrix that results from the attention mechanism.

        Returns:
            tuple: The Output matrix and its label.
        """
        output_matrix = Matrix([[2.6, 3.4], [2.0, 2.5]], h_buff=1.5)
        output_label = Text("Output", font_size=24).next_to(output_matrix, UP)
        output_matrix.next_to(self.attention_scores, DOWN, buff=1.5)
        
        return output_matrix, output_label

    def display_output(self, output_label, output_matrix):
        """
        Displays the Output matrix with its label.

        Args:
            output_label: The label for the Output matrix.
            output_matrix: The Output matrix itself.
        """
        self.play(Write(output_label), Write(output_matrix))
        self.wait(2)

    def add_arrows(self, query_matrix, key_matrix, attention_scores, output_matrix):
        """
        Adds arrows to show the flow between matrices.

        Args:
            query_matrix, key_matrix: Matrices that are involved in the attention computation.
            attention_scores: The matrix that holds the computed attention scores.
            output_matrix: The final output matrix resulting from the attention mechanism.
        """
        self.play(
            GrowArrow(Arrow(query_matrix.get_bottom(), attention_scores.get_top(), buff=0.2)),
            GrowArrow(Arrow(key_matrix.get_bottom(), attention_scores.get_top(), buff=0.2)),
            GrowArrow(Arrow(attention_scores.get_bottom(), output_matrix.get_top(), buff=0.2)),
        )
        self.wait(2)
