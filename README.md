# Image Analysis API

A FastAPI backend service that allows uploading images and performing mock analysis.

## 🚀 Live Demo & Documentation

**Live Swagger UI:** http://personal-image-api-amfnxc-be0ca7-72-62-20-215.traefik.me/docs
**Test API Key:** `dev-api-key-123`

1. Go to the link above.
2. Click **Authorize**.
3. Enter the API key: `dev-api-key-123`.

_Local docs available at `http://localhost:8000/docs` when running locally._

## Running the Service

### Option 1: Local Development (uv)

**Prerequisites:**

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

**Install dependencies:**

```bash
uv sync
```

**Run the server:**

```bash
uv run fastapi dev app/main.py
```

The API will be available at `http://localhost:8000`

---

### Option 2: Docker

**Build the image:**

```bash
docker build -t image-api .
```

**Run the container:**

```bash
docker run -p 8000:80 -e API_KEY=your-secret-key image-api
```

The API will be available at `http://localhost:8000`

## Authentication

All endpoints (except health check) require an API key passed via the `X-API-Key` header.

**Default development key:** `dev-api-key-123`

For production, set the `API_KEY` environment variable:

```bash
API_KEY=your-secret-key uv run fastapi dev app/main.py
```

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
  -H "X-API-Key: dev-api-key-123" \
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
  -H "X-API-Key: dev-api-key-123" \
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
| 401         | Missing API key                     |
| 403         | Invalid API key                     |
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
4. **Authentication**: Add JWT-based authentication with refresh tokens
5. **Rate Limiting**: Prevent abuse with request rate limiting
6. **Caching**: Use Redis instead of local JSON file for result caching
7. **Background Processing**: Use Celery for async analysis of large images
8. **Monitoring**: Add Prometheus metrics and structured logging
9. **Testing**: Add comprehensive unit and integration tests

## Project Structure

```
image-api/
├── Dockerfile
├── .dockerignore
├── pyproject.toml
├── uv.lock
├── README.md
└── app/
    ├── main.py               # FastAPI application entry point
    ├── config.py             # Configuration settings
    ├── auth.py               # API key authentication
    ├── routes/
    │   └── image.py          # Route handlers
    ├── services/
    │   ├── upload_service.py     # File upload logic
    │   ├── analysis_service.py   # Mock analysis logic
    │   └── storage_service.py    # Result caching
    ├── schemas/
    │   └── image.py          # Pydantic models
    └── utils/
        └── file_utils.py     # Utility functions
```
