## Test Coverage
Here is my test coverage when I ran pytest on the 11 test I had on my test_app.py

***********************************************************************
=============================================== tests coverage =============================================== 
______________________________ coverage: platform win32, python 3.10.16-final-0 ______________________________ 

Name          Stmts   Miss  Cover
---------------------------------
app\main.py      69     10    86%
---------------------------------
TOTAL            69     10    86%
============================================ 11 passed in 15.66s =============================================



## Build/run Commands
I had many issues building it. 

First it kept erroring around the 8/11 docker build progress, due to I think the image size being too big. So I had to add /data and the model into .Dockerignore as well, to make the image size smaller, since I knew eventually I will be linking the model.json from the GCP Bucket I created anyways.

Next I had issues even re-building it after it kept getting hung up in terminal and stuck, and then docker desktop wouldn't start the engine no matter how many time i restarted the docker desktop application. After doing many different things, the fix was simply restarting my computer, and docker desktop was working again, and I was able to manually delete the incomplete image that was on their from my failed build.

Next upon re-building the docker image, it now failed at the 10/11 progress bar. So I had to use the prune command and delete the volume. I also noticed my computer disk drive had only 2 gigs on it and was wondering if that caused the issue by constantly running out of space. So I cleared more space and tried the build again with 10.2 gigs, and now the completed successfully finally.

I then tested by running the Docker image, and opening it in the port 8080 on my browers and did a health check and inspected the browser and everything seems to be running well.

***********************************************************************

PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> docker build -t penguin-app .                        
>>
[+] Building 265.3s (11/11) FINISHED                                                      docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                      0.1s
 => => transferring dockerfile: 503B                                                                      0.1s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                       0.9s
 => [auth] library/python:pull token for registry-1.docker.io                                             0.0s
 => [internal] load .dockerignore                                                                         0.1s
 => => transferring context: 159B                                                                         0.0s 
 => [internal] load build context                                                                         0.7s 
 => => transferring context: 205.54kB                                                                     0.4s
 => [1/5] FROM docker.io/library/python:3.10-slim@sha256:81f1cdb3770d54ecfdbddcc52c2125fce674c14a1d976df  0.2s
 => => resolve docker.io/library/python:3.10-slim@sha256:81f1cdb3770d54ecfdbddcc52c2125fce674c14a1d976df  0.2s
 => CACHED [2/5] WORKDIR /app                                                                             0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                  0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                            111.6s
 => [5/5] COPY . .                                                                                        1.2s
 => ERROR exporting to image                                                                            150.1s 
 => => exporting manifest sha256:0b362a160d348ae9f45ae7e838d1848f93f6cd613992affad866490a23782664         0.1s 
 => => exporting config sha256:b08a3195b040b8fe64a6fdc59a22ddb6906c6dde3b42068618bacca13ace7b29           0.1s 
 => => exporting attestation manifest sha256:fe2adf82fed22f2b930a27bde17b8bffa056f89a9c5fd57f5699d4740d1  0.6s 
 => => exporting manifest list sha256:3918949a74e4922068820a4c6ef0c338926b9241a91b43d1fff7826c17589a62    0.1s 
 => => naming to docker.io/library/penguin-app:latest                                                     0.1s 
 => => unpacking to docker.io/library/penguin-app:latest                                                 30.9s 
------
 > exporting to image:
------
ERROR: failed to build: failed to solve: failed to extract layer sha256:b98b16ec04672583d7f711a39f58f9fc29d8e504d449084ddb8079ccda9ddce0: write /var/lib/desktop-containerd/daemon/io.containerd.snapshotter.v1.overlayfs/snapshots/254/fs/usr/local/lib/python3.10/site-packages/nvidia/nccl/lib/libnccl.so.2: input/output error
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> docker system prune -a --volumes
>> 
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all anonymous volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
Deleted Networks:
assignment-1_0076f1_airflow

Deleted Images:
untagged: penguin-app:latest
deleted: sha256:3918949a74e4922068820a4c6ef0c338926b9241a91b43d1fff7826c17589a62
deleted: sha256:0b362a160d348ae9f45ae7e838d1848f93f6cd613992affad866490a23782664
deleted: sha256:b08a3195b040b8fe64a6fdc59a22ddb6906c6dde3b42068618bacca13ace7b29
deleted: sha256:fe2adf82fed22f2b930a27bde17b8bffa056f89a9c5fd57f5699d4740d1a02c9
deleted: sha256:9c25120fd2fcc49d3cb3152a6689860c5cfdb3f2279e3626f66aa6ccfa2b5f65
deleted: sha256:f4f9f9c044a97d1c3affe18ba7df3d7cea89506a5598f616693e5f50ddd8688c

Deleted build cache objects:
hn4uzvn225ptbwj05nwivular
pg9nv7g3q1nm1v7v5tdlei22h
z0nd69gyo71s39tmjiabjy6hk
fkdwm8hydxx36imlhypenbqpk
zbl6lp64nvoiku3vbc62mkno0
wnbnssc2ju53xgce1r9frm1me
oj0scecpepdi20deh4k4okljt
k2c8i18s48nou6ozi3pgeu4ha
037hpawb7m1pkhl1p5lf7bo4i
nngopy41iu8q9wjq71uegd6sa
ko77hchhoqhud88j1j1467x13
j6hhenoh1slf4g1i2vcrq0axw
gi68k055ftia1p5t9ez3xg52q
jogm1cfbejykqef9r6byrndxk
sod5ojbayync4ldurjtpo0rzy
tanny8aullx4unhg466o08ggn
l376nt0peja9ke0bsgu63md7o
rilq5hngdparxo2tssmad34ek
yjupe5a4mrvx1za3b12h3mx4j
igl0frphnxiqf1jwa33c1x1a3
26t675dfwq022i6tnth9kcaok
pmufkgsbo8ihzq0dz3p1i9msj
imxepv15sosmlmhfrbyitt84h
yxdm0efm9ty20npqzy0clqo28
pzant7zzdxzwz3mv8sclm60f7
8la15ed3u7fkloa3r30opyji7
s55vasn3do09h1762l3sbn48q
nj31gstup4guzfltv4cns9lpo
s44i5zvhmzpd0exwis6a5kh7z
v7cf8jfu2r8qa0mh1ynh7e7s8
q0wte1je69un54wihvmir2joq
0cam56vu02qcz30zn6c904qgd
xky6vz6x25ar4q0k8a5i4zqa6
qpat17qt22unk70tnxcn3bebs
mpanmq7ocnh9xioglyjxapi50
yygdtv7hbw2scmh73r9s0pve7
az2plhiagtx9i99l9bqov294c
rzstk52gzqqgsq2vz1z4au0gk
mpz1hzcf72hq8k4dz6xjkcn3b
x0dnvogly6a8v7ly1ncn0cbtt
rv3tx7z2u7yp2hf1eyvugbdcu
cclb64az5gxbvp0jmopgr6rj3
xzwsidrpye7cj5unypexzvqwp
jx1wavcq68y6z1949ihaxclgj
qwaokwvudrlv42t1d45lw6yho
nb0ip9sdvc286i9ajfma5wnua
vnjo2eg0ol9ddpq7a1dhrrchl
14wcby5nb69oc723cp8efmfu5
w5uaapoef0cr5g3trw7jpuavl
m6ohkod05xozrkxvxppt18868
ln4f37k80uovio534cxc6292x
tsmn4oec5w1jwx02vx3uhus8g
lpm5bgbmk6oo8dri8b81b8byz

Total reclaimed space: 3.685GB
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> docker build -t penguin-app .   
>> 
[+] Building 249.3s (11/11) FINISHED                                                      docker:desktop-linux 
 => [internal] load build definition from Dockerfile                                                      0.2s 
 => => transferring dockerfile: 503B                                                                      0.0s 
 => [internal] load metadata for docker.io/library/python:3.10-slim                                       2.2s 
 => [auth] library/python:pull token for registry-1.docker.io                                             0.0s 
 => [internal] load .dockerignore                                                                         0.1s 
 => => transferring context: 159B                                                                         0.0s 
 => [1/5] FROM docker.io/library/python:3.10-slim@sha256:81f1cdb3770d54ecfdbddcc52c2125fce674c14a1d976df  7.4s 
 => => resolve docker.io/library/python:3.10-slim@sha256:81f1cdb3770d54ecfdbddcc52c2125fce674c14a1d976df  0.2s
 => => sha256:12b8240e46e9f448e7eba19870e233d03c7160ca9b1777ab3ec2eeddf4349fa8 3.51MB / 3.51MB            1.0s
 => => sha256:00aa2453f38062a311a828d4d0790d1911a81372ad928c8856387ceccc7a6c12 250B / 250B                0.3s
 => => sha256:3fa1124e7cf3ed5061a51b47c3e7a138e1b25dce3c94e9967a6b2a9acfe36402 15.65MB / 15.65MB          2.7s
 => => sha256:59e22667830bf04fb35e15ed9c70023e9d121719bb87f0db7f3159ee7c7e0b8d 28.23MB / 28.23MB          3.4s
 => => extracting sha256:59e22667830bf04fb35e15ed9c70023e9d121719bb87f0db7f3159ee7c7e0b8d                 1.7s
 => => extracting sha256:12b8240e46e9f448e7eba19870e233d03c7160ca9b1777ab3ec2eeddf4349fa8                 0.3s
 => => extracting sha256:3fa1124e7cf3ed5061a51b47c3e7a138e1b25dce3c94e9967a6b2a9acfe36402                 1.1s 
 => => extracting sha256:00aa2453f38062a311a828d4d0790d1911a81372ad928c8856387ceccc7a6c12                 0.1s 
 => [internal] load build context                                                                         0.6s 
 => => transferring context: 286.59kB                                                                     0.5s 
 => [3/5] COPY requirements.txt .                                                                         0.3s 
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                            138.3s 
 => [5/5] COPY . .                                                                                        0.4s 
 => exporting to image                                                                                   99.4s 
 => => exporting layers                                                                                  75.1s 
 => => exporting manifest sha256:7316885f29fb558129b839efa8806cb92de86c052a72d3f65b0091ba65893b14         0.0s 
 => => exporting config sha256:5d7bb95409b2a90ecc13ae93792cfe51b80ff9e7ca9bebe9a3311cbafaaa84b8           0.0s 
 => => exporting attestation manifest sha256:916eaed6f46a2676e66523fa26978c55097fdec3524bb5494f5f67adfd7  0.2s 
 => => exporting manifest list sha256:f576227a48e676d114b0b97a767dc63ba960309357c9fba71373d4c8ce42bb2a    0.1s 
 => => naming to docker.io/library/penguin-app:latest                                                     0.0s 
 => => unpacking to docker.io/library/penguin-app:latest                                                 23.7s 

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/y85ejbmbogi1g3dy6zz8pwuzy     
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> docker run -p 8080:8080 penguin-app
2025-08-06 00:31:38,127 - INFO - Loading model from /app/app/data/model.json
2025-08-06 00:31:38,135 - INFO - Model loaded successfully
INFO:     Started server process [1]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     172.17.0.1:57784 - "GET / HTTP/1.1" 200 OK
INFO:     172.17.0.1:57784 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     172.17.0.1:49648 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:49648 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:39020 - "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 Not Found    
INFO:     172.17.0.1:33034 - "GET /health HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]



## Docker Inspect
Here is details on my built docker image when I ran the docker inspect command:

************************************************************************************
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> docker inspect penguin-app
>>
[
    {
        "Id": "sha256:f576227a48e676d114b0b97a767dc63ba960309357c9fba71373d4c8ce42bb2a",
        "RepoTags": [
            "penguin-app:latest"
        ],
        "RepoDigests": [
            "penguin-app@sha256:f576227a48e676d114b0b97a767dc63ba960309357c9fba71373d4c8ce42bb2a"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-08-06T00:26:34.492207568Z",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 766507299,
        "GraphDriver": {
            "Data": null,
            "Name": "overlayfs"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:7cc7fe68eff66f19872441a51938eecc4ad33746d2baa3abc081c1e6fe25988e",
                "sha256:d379451f91b6692e0a2247328d637db8e27c47855dc41f3014de5118c5550cfe",
                "sha256:3ba4af0751c6e06b532dda1b0ecd0f858be0a6cee1cfb7c56ebedb889b0b9471",
                "sha256:f6dc80d9d1672208bdb0b4dc574353d3748880680861cd537850080e37470692",
                "sha256:a6ef9ceb7d4964bb8c94d0aac81285b96ed041f55de9f204cc6eae9220664eff",
                "sha256:5902aebd6dad653293feeffbc570e1ec97f63d64835a6abfb738d9d7637bc574",
                "sha256:968723913896e1c4e6809a0dc8380e3805d956cb6471dcae54e0022ace72698f",
                "sha256:fe399c1443ad6d1c62c278879ed075bb6212ba318f64572f4d10470009e53f3f"
            ]
        },
        "Metadata": {
            "LastTagTime": "2025-08-06T00:27:50.105907073Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:f576227a48e676d114b0b97a767dc63ba960309357c9fba71373d4c8ce42bb2a",
            "size": 856
        },
        "Config": {
            "ArgsEscaped": true,
            "Cmd": [
                "uvicorn",
                "app.main:app",
                "--host",
                "0.0.0.0",
                "--port",
                "8080"
            ],
            "Entrypoint": null,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.10.18",
                "PYTHON_SHA256=ae665bc678abd9ab6a6e1573d2481625a53719bc517e9a634ed2b9fefae3817f"
            ],
            "ExposedPorts": {
                "8080/tcp": {}
            },
            "Labels": null,
            "OnBuild": null,
            "User": "",
            "Volumes": null,
                "PYTHON_VERSION=3.10.18",
                "PYTHON_SHA256=ae665bc678abd9ab6a6e1573d2481625a53719bc517e9a634ed2b9fefae3817f"
            ],
            "ExposedPorts": {
                "8080/tcp": {}
            },
            "Labels": null,
            "OnBuild": null,
            "User": "",
                "PYTHON_VERSION=3.10.18",
                "PYTHON_SHA256=ae665bc678abd9ab6a6e1573d2481625a53719bc517e9a634ed2b9fefae3817f"
            ],
            "ExposedPorts": {
                "8080/tcp": {}
            },
                "PYTHON_VERSION=3.10.18",
                "PYTHON_SHA256=ae665bc678abd9ab6a6e1573d2481625a53719bc517e9a634ed2b9fefae3817f"
            ],
            "ExposedPorts": {
                "8080/tcp": {}
                "PYTHON_VERSION=3.10.18",
                "PYTHON_SHA256=ae665bc678abd9ab6a6e1573d2481625a53719bc517e9a634ed2b9fefae3817f"
                "PYTHON_SHA256=ae665bc678abd9ab6a6e1573d2481625a53719bc517e9a634ed2b9fefae3817f"
            ],
            "ExposedPorts": {
                "8080/tcp": {}
            },
            "Labels": null,
            "OnBuild": null,
            "User": "",
            "Volumes": null,
            "WorkingDir": "/app"
        }
    }
]



## Model Loading Locally
Model loaded and running locally successfully:

****************************************
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
>> 
Using CPython 3.10.16
Creating virtual environment at: .venv
Installed 47 packages in 9.59s
INFO:     Will watch for changes in these directories: ['C:\\Users\\agila\\Documents\\AIDI 2004\\Assignment2\\demo-1']
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [10908] using StatReload
2025-08-05 22:07:03,249 - INFO - Loading model from C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1\app\data\model.json
2025-08-05 22:07:03,266 - INFO - Model loaded successfully
INFO:     Started server process [7716]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:54353 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:54354 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:54354 - "GET /openapi.json HTTP/1.1" 200 OK



## Ensure the model loads from Google Cloud Storage using the service account
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
>> 
INFO:     Will watch for changes in these directories: ['C:\\Users\\agila\\Documents\\AIDI 2004\\Assignment2\\demo-1']
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [9200] using StatReload
2025-08-05 23:00:45,013 - INFO - Attempting to load model from GCS: bucket=penguin-backend-bucket blob=model.json
2025-08-05 23:00:45,527 - INFO - Model loaded from GCS successfully
INFO:     Started server process [14064]
INFO:     Waiting for application startup.
INFO:     Application startup complete.



## Test in Container:
My app now work in a docker container and is using the GCP Bucket model:
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> docker run -p 8080:8080 `    
>>   -v "C:\Users\agila\Documents\AIDI` 2004\Assignment2\demo-1\sa-key.json:/gcp/sa-key.json:ro" `
>>   -e GOOGLE_APPLICATION_CREDENTIALS=/gcp/sa-key.json `
>>   -e GCS_BUCKET_NAME=penguin-backend-bucket `
>>   -e GCS_BLOB_NAME=model.json `
>>   penguin-app
>>
et `\x0a  -e GCS_BLOB_NAME=model.json `\x0a  penguin-app\x0a;9896213f-2ab9-4555-93c0-2cae948d50d0Downloading cpython-3.10.16-linux-x86_64-gnu (download) (19.8MiB)
 Downloading cpython-3.10.16-linux-x86_64-gnu (download)
Using CPython 3.10.16
Removed virtual environment at: .venv
Creating virtual environment at: .venv
Downloading pygments (1.2MiB)
Downloading pandas (12.5MiB)
Downloading kiwisolver (1.6MiB)
Downloading nvidia-nccl-cu12 (307.4MiB)
Downloading matplotlib (8.2MiB)
Downloading xgboost (242.1MiB)
Downloading fonttools (4.5MiB)
Downloading pydantic-core (1.9MiB)
Downloading scipy (35.9MiB)
Downloading pillow (6.3MiB)
Downloading numpy (15.7MiB)
Downloading scikit-learn (12.3MiB)
 Downloading pygments
 Downloading kiwisolver
 Downloading pydantic-core
 Downloading fonttools
 Downloading pillow
 Downloading matplotlib
 Downloading scikit-learn
 Downloading numpy
 Downloading pandas
 Downloading scipy
 Downloading xgboost
 Downloading nvidia-nccl-cu12
Installed 63 packages in 438ms
2025-08-06 03:51:36,698 - INFO - Attempting to load model from GCS: bucket=penguin-backend-bucket blob=model.json
2025-08-06 03:51:37,303 - INFO - Model loaded from GCS successfully
INFO:     Started server process [72]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     172.17.0.1:43844 - "GET / HTTP/1.1" 200 OK
INFO:     172.17.0.1:53242 - "GET / HTTP/1.1" 200 OK
INFO:     172.17.0.1:53246 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:53246 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:59290 - "GET /health HTTP/1.1" 200 OK



## Artifact Registry repository created and accessible
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> docker push us-central1-docker.pkg.dev/penguin-features/penguin-backend-artifact/penguin-app:latest
The push refers to repository [us-central1-docker.pkg.dev/penguin-features/penguin-backend-artifact/penguin-app]
59e22667830b: Pushed
d7606484c059: Pushed
12b8240e46e9: Pushed
3fa1124e7cf3: Pushed
9efa460adf91: Pushed
2e0ad8305c1d: Pushed
d4c14146648e: Pushed
2a320db1ea36: Pushed
00aa2453f380: Pushed
e207db738480: Pushed
latest: digest: sha256:7c883126c59a53a296deadccd9067cf85da70891286b81ce5131aaecb473cfc0 size: 856



## Deployed to cloud run
It all works, this is the url: https://penguin-backend-cloudran-151607684225.us-central1.run.app

I also test the /docs, and used curl command bellow to test the endpoint predict. It gave me the correct prediction when I wrote "Male" for sex, gave me the correct error when I wrote "tree" for sex, and finally gave me the correct prediction again when I wrote "Female" for sex.

************************************************************************
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> Invoke-RestMethod -Uri "https://penguin-backend-cloudran-151607684225.us-central1.run.app/predict" `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"bill_length_mm": 45.5, "bill_depth_mm": 14.2, "flipper_length_mm": 210, "body_mass_g": 4200, "year": 2007, "sex": "Male", "island": "Biscoe"}'
>> 
   ody_mass_g": 4200, "year": 2007, "sex": "Male", "island": "Biscoe"}'\x0a;9896213f-2ab9-4555-93c0-2cae948d50d0
----------
         2


PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> Invoke-RestMethod -Uri "https://penguin-backend-cloudran-151607684225.us-central1.run.app/predict" `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"bill_length_mm": 45.5, "bill_depth_mm": 14.2, "flipper_length_mm": 210, "body_mass_g": 4200, "year": 2007, "sex": "tree", "island": "Biscoe"}'
>> 
   ody_mass_g": 4200, "year": 2007, "sex": "tree", "island": "Biscoe"}'\x0a;9896213f-2ab9-4555-93c0-2cae948d50dInvoke-RestMethod : {"detail":[{"type":"enum","loc":["body","sex"],"msg":"Input should be 'Male' or 
'Female'","input":"tree","ctx":{"expected":"'Male' or 'Female'"}}]}
At line:1 char:1
+ Invoke-RestMethod -Uri "https://penguin-backend-cloudran-151607684225 ...
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod  
   ], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCom  
   mand
PS C:\Users\agila\Documents\AIDI 2004\Assignment2\demo-1> Invoke-RestMethod -Uri "https://penguin-backend-cloudran-151607684225.us-central1.run.app/predict" `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"bill_length_mm": 45.5, "bill_depth_mm": 14.2, "flipper_length_mm": 210, "body_mass_g": 4200, "year": 2007, "sex": "Female", "island": "Biscoe"}'
>>                      ody_mass_g": 4200, "year": 2007, "sex": "Female", "island": "Biscoe"}'\x0a;9896213f-2ab9-4555-93c0-2cae948d50d0

prediction
----------
         2
