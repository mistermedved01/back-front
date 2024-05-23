FROM node:19-alpine as builder
COPY ./ /build/
WORKDIR /build/
RUN yarn install && yarn build

FROM node:19-alpine as scratch
#ENV HOST="0.0.0.0"
COPY --from=builder /build/.output/ /app/
CMD node /app/server/index.mjs
EXPOSE 3000