FROM python:3.13.11-slim

#Copy the uv binary from the uv image to the /bin/ directory of the current image 
#ghcr.io/astral-sh/uv:latest is the official source image for uv, which is a tool for managing Python dependencies and virtual environments. By copying the uv binary from the source image to the /bin/ directory of the current image, we can use uv to manage our Python dependencies in this Docker container.

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

#RUN pip install pandas pyarrow

WORKDIR  /code

# set the PATH environment variable to include the .venv/bin directory, which is where the uv tool will create a virtual environment for our project. This allows us to use the uv tool and any dependencies installed in the virtual environment without having to specify the full path to the executable.

ENV PATH="/code/.venv/bin:$PATH" 

COPY pyproject.toml .python-version uv.lock ./

COPY  ingest_data.py .

#--locked flag ensures that the exact versions of the dependencies specified in the uv.lock file are installed, which helps to ensure consistency and reproducibility of the environment.

RUN  uv sync --locked #--locked flag ensures that the exact versions of the dependencies specified in the uv.lock file are installed, which helps to ensure consistency and reproducibility of the environment.

COPY pipeline.py .
ENTRYPOINT ["python", "pipeline.py"]