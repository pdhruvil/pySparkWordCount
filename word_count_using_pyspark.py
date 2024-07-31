import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split


def main(input_path, output_path):
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("WordCount") \
        .getOrCreate()

    # Read the input text file from Google Cloud Storage
    df = spark.read.text(input_path)

    # Split the lines into words
    words = df.select(explode(split(df.value, " ")).alias("word"))

    # Count the occurrences of each word
    word_counts = words.groupBy("word").count()

    # Write the output to Google Cloud Storage
    word_counts.write.csv(output_path, header=True)

    # Stop the Spark session
    spark.stop()


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Word Count in PySpark")
    parser.add_argument("input_path", type=str, help="Input path (GCS URL, e.g., gs://your-bucket-name/input.txt)")
    parser.add_argument("output_path", type=str, help="Output path (GCS URL, e.g., gs://your-bucket-name/output)")

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the provided arguments
    main(args.input_path, args.output_path)
