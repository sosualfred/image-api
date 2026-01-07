# Image Analysis API

A FastAPI backend service that allows uploading images and performing mock analysis.

## Setup

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
uv sync
```

## Running the Service

```bash
uv run fastapi dev app/main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Upload Image

Upload an image for analysis.

**Endpoint:** `POST /upload`

**Request:**

- Content-Type: `multipart/form-data`
- Body: `file` (JPEG or PNG, max 5MB)

**Response:**

```json
{
  "image_id": "abc123def456"
}
```

**Example:**

```bash
curl -X POST "http://localhost:8000/upload" \
  -F "file=@/path/to/image.jpg"
```

---

### Analyze Image

Analyze a previously uploaded image.

**Endpoint:** `POST /analyze`

**Request:**

```json
{
  "image_id": "abc123def456"
}
```

**Response:**

```json
{
  "image_id": "abc123def456",
  "skin_type": "Oily",
  "issues": ["Hyperpigmentation", "Acne"],
  "confidence": 0.87
}
```

**Example:**

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"image_id": "abc123def456"}'
```

---

### Health Check

**Endpoint:** `GET /`

**Response:**

```json
{
  "message": "Image Analysis API",
  "version": "1.0.0"
}
```

## Error Handling

| Status Code | Description                         |
| ----------- | ----------------------------------- |
| 400         | Invalid file type or file too large |
| 404         | Image not found                     |
| 500         | Internal server error               |

## Assumptions

- Images are stored locally in the `uploads/` directory
- Analysis is mocked with random skin types and issues
- Image IDs are 12-character hex strings
- Only JPEG and PNG formats are accepted

## Production Improvements

If this were a production service, I would:

1. **Database Integration**: Store image metadata in PostgreSQL/MongoDB with proper indexing
2. **Cloud Storage**: Use AWS S3 or GCS instead of local filesystem
3. **Real AI Integration**: Connect to a trained ML model for actual skin analysis
4. **Authentication**: Add JWT-based authentication and API keys
5. **Rate Limiting**: Prevent abuse with request rate limiting
6. **Caching**: Cache analysis results with Redis
7. **Background Processing**: Use Celery for async analysis of large images
8. **Monitoring**: Add Prometheus metrics and structured logging
9. **Testing**: Add comprehensive unit and integration tests
10. **Docker**: Containerize the application for consistent deployments

## Project Structure

```
app/
├── main.py           # FastAPI application entry point
├── config.py         # Configuration settings
├── routes/
│   └── image.py      # Route handlers
├── services/
│   ├── upload_service.py    # File upload logic
│   └── analysis_service.py  # Mock analysis logic
├── schemas/
│   └── image.py      # Pydantic models
└── utils/
    └── file_utils.py # Utility functions
```
