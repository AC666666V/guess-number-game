FROM kivy/buildozer

WORKDIR /app

COPY . .

RUN buildozer android debug