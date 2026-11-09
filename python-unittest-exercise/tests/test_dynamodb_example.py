
import boto3
import pytest
from moto import mock_dynamodb2
from botocore.exceptions import ParamValidationError

from src.boto3_example import DynamodBExample


@mock_dynamodb2
def test_create_dynamo_table():
    dynamodb_example = DynamodBExample()

    # Create the Movies table
    dynamodb_example.create_movies_table()

    # Access the created table
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Movies')

    # Verify table creation
    assert table.table_status == 'ACTIVE'
    assert table.key_schema == [
        {'AttributeName': 'year', 'KeyType': 'HASH'},
        {'AttributeName': 'title', 'KeyType': 'RANGE'}
    ]


@mock_dynamodb2
def test_add_dynamo_record_table():
    dynamodb_example = DynamodBExample()

    # Create the table first
    dynamodb_example.create_movies_table()

    # Prepare a movie record
    movie = {
        'year': 2024,
        'title': 'Inception'
    }

    # Insert the record
    dynamodb_example.add_dynamo_record('Movies', movie)

    # Retrieve the inserted record
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Movies')

    response = table.get_item(
        Key={
            'year': 2024,
            'title': 'Inception'
        }
    )

    # Verify the record
    assert response['Item'] == movie


@mock_dynamodb2
def test_add_dynamo_record_table_failure():
    dynamodb_example = DynamodBExample()

    # Create the table first
    dynamodb_example.create_movies_table()

    # Pass invalid input instead of a dictionary
    invalid_item = 'invalid_movie_record'

    # Verify that boto3 raises a validation error
    with pytest.raises(ParamValidationError):
        dynamodb_example.add_dynamo_record('Movies', invalid_item)
