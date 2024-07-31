# Word Count in PySpark

This project implements a simple word count application using PySpark. It reads a text file from Google Cloud Storage (GCS), counts the occurrences of each word, and writes the results back to GCS in CSV format.

## Prerequisites

- Python 3.x
- Apache Spark
- PySpark
- Google Cloud SDK (for accessing Google Cloud Storage)
- Access to a Google Cloud Storage bucket

## Installation

1. **Install PySpark**: You can install PySpark using pip:

   ```bash
   pip install pyspark
   ```

2. **Set up Google Cloud SDK**: Follow the instructions on the [Google Cloud SDK documentation](https://cloud.google.com/sdk/docs/install) to install and configure the SDK.

## Usage

To run the word count application, use the following command:

```bash
python word_count.py <input_path> <output_path>
```

### Arguments

- `input_path`: The path to the input text file in Google Cloud Storage. It should be in the format `gs://your-bucket-name/input.txt`.
- `output_path`: The path where the output CSV file will be saved in Google Cloud Storage. It should be in the format `gs://your-bucket-name/output`.

### Example

```bash
python word_count.py gs://your-bucket-name/input.txt gs://your-bucket-name/output
```

## Code Explanation

- **Spark Session**: The application initializes a Spark session with the name "WordCount".
- **Reading Input**: It reads the input text file from the specified GCS path.
- **Word Splitting**: The lines are split into individual words using the `split` and `explode` functions.
- **Counting Words**: The application groups the words and counts their occurrences.
- **Writing Output**: The results are written to the specified output path in CSV format, including a header row.
- **Stopping Spark**: Finally, the Spark session is stopped to free up resources.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [Apache Spark](https://spark.apache.org/)
- [Google Cloud Storage](https://cloud.google.com/storage)

Feel free to contribute to this project by submitting issues or pull requests!