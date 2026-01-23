# Production-Grade MLOps pipeline with CI/CD for Heart Disease Model using GitHub Actions and GCP

**Objective:** Developed and deployed a production-ready, explainable, observable, scalable, and maintainable MLOps pipeline for a heart disease prediction model using a CI/CD process.

**Tech Stack:** GCP, Kubernetes GKE, Docker, GitHub Actions, FastAPI, SHAP, Work, Kolmogorov–Smirnov (KS) test, Google Artifact Registry, EC2 E2 Standard Instance.

**Design and Methodology:**

  * **Model Explainability & Fairness:** Used SHAP values to identify key features (CP, CA, OLP) influencing false negatives. Checked fairness with age (20-year bins) as a sensitive attribute, finding low prediction accuracy for the 20 to 40 age group.
  * **Production and Deployment:** Trained and saved the model (addressing data imbalance). Created a FastAPI server and Dockerized the application (Python 3.10 slim, port 8000).
  * **CI/CD:** Implemented CI/CD using GitHub Actions, triggered on pushes/PRs to the main branch, which built, tagged, and pushed the Docker image to Google Artifact Registry.
  * **Kubernetes Deployment:** Deployed the image to a Kubernetes GKE cluster with a maximum of three pods for scaling.

**Outcomes:**

  * **Observability:** Implemented per-sample prediction logging using a 100-row randomly generated dataset.
  * **Performance:** Performed load testing with 'Work' (50 threads, 2,500 connections). Handled 59,000 requests in 30 seconds with an average latency of 144.43 milliseconds.
  * **Drift Detection:** Computed input drift between training data and randomly generated data using the KS test, successfully detecting drift in features like 'age'.
  * Successfully created a complete and observable CI/CD pipeline for the ML model.

## How to run / Use this project

### Local (Python)

- Requirements: Python 3.9+ and `api/model.joblib` available in the `api/` folder.
- From repository root:

```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# Windows PowerShell
. .venv\Scripts\Activate.ps1
pip install -r api/requirements.txt
cd api
python -m uvicorn api:app --host 0.0.0.0 --port 8000
```

Test the health endpoint:

```bash
curl http://127.0.0.1:8000/
```

Example prediction request (adjust features as needed):

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":63,"gender":0,"cp":3,"trestbps":145,"chol":233,"fbs":1,"restecg":0,"thalach":150,"exang":0,"oldpeak":2.3,"slope":0,"ca":0,"thal":1}'
```

### Docker

Build and run the container (from repo root):

```bash
docker build -t heart-api api/.
docker run -p 8000:8000 --rm heart-api
```

Then call the same endpoints at `http://127.0.0.1:8000`.

### CI/CD (GitHub Actions → GCP Artifact Registry / GKE)

- Required repository Secrets (set in GitHub Settings → Secrets):
  - `GCP_CREDENTIALS_B64` (base64-encoded service account JSON)
  - `GCP_PROJECT_ID` (project id) — the workflow now reads this from secrets.
- The workflow `.github/workflows/cd.yml` builds and pushes the Docker image to Artifact Registry.

### Notes & recommendations before making repo public
- Do NOT commit service account JSON or other credentials. Use GitHub Secrets as shown.
- Consider adding `api/model.joblib` and large notebook outputs to `.gitignore` and storing the model in a private artifact store (Artifact Registry / Cloud Storage).
- Clear notebook outputs (remove large base64 images) to reduce repo size and avoid leaking data.

If you want, I can add a `.gitignore` entry for `api/model.joblib` and strip outputs from notebooks automatically.
