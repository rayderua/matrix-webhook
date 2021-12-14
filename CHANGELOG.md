# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- join room before sending message
  in [#12](https://github.com/zerodotfive/matrix-webhook/pull/12)
  by [@bboehmke](https://github.com/bboehmke)

## [v3.2.1] - 2021-08-28

- fix changelog

## [v3.2.0] - 2021-08-27

- add github & grafana formatters
- add formatted_body to bypass markdown with direct
  [matrix-custom-HTML](https://matrix.org/docs/spec/client_server/r0.6.1#m-room-message-msgtypes)
- allow "key" to be passed as a parameter
- allow to use a sha256 HMAC hex digest with the key instead of the raw key
- allow "room_id" to be passed as a parameter or with the data
- rename "text" to "body".
- Publish releases also on github from github actions
- fix tests for recent synapse docker image

## [v3.1.1] - 2021-07-18

## [v3.1.0] - 2021-07-18

- Publish on PyPI & Docker Hub with Github Actions
  in [#10](https://github.com/zerodotfive/matrix-webhook/pull/10)
  by [@zerodotfive](https://github.com/zerodotfive)

## [v3.0.0] - 2021-07-18

- Simplify code
  in [#1](https://github.com/zerodotfive/matrix-webhook/pull/1)
  by [@homeworkprod](https://github.com/homeworkprod)
- Update aiohttp use and docs
  in [#5](https://github.com/zerodotfive/matrix-webhook/pull/5)
  by [@svenseeberg](https://github.com/svenseeberg)
- Setup Tests, Coverage & CI ; update tooling
  in [#7](https://github.com/zerodotfive/matrix-webhook/pull/7)
  by [@zerodotfive](https://github.com/zerodotfive)
- Setup argparse & logging
  in [#8](https://github.com/zerodotfive/matrix-webhook/pull/8)
  by [@zerodotfive](https://github.com/zerodotfive)
- Setup packaging
  in [#9](https://github.com/zerodotfive/matrix-webhook/pull/9)
  by [@zerodotfive](https://github.com/zerodotfive)

## [v2.0.0] - 2020-03-14
- Update to matrix-nio & aiohttp & markdown

## [v1.0.0] - 2020-02-14
- First release with matrix-client & http.server

[Unreleased]: https://github.com/zerodotfive/matrix-webhook/compare/v3.2.1...master
[v3.2.1]: https://github.com/zerodotfive/matrix-webhook/compare/v3.2.0...v3.2.1
[v3.2.0]: https://github.com/zerodotfive/matrix-webhook/compare/v3.1.1...v3.2.0
[v3.1.1]: https://github.com/zerodotfive/matrix-webhook/compare/v3.1.0...v3.1.1
[v3.1.0]: https://github.com/zerodotfive/matrix-webhook/compare/v3.0.0...v3.1.0
[v3.0.0]: https://github.com/zerodotfive/matrix-webhook/compare/v2.0.0...v3.0.0
[v2.0.0]: https://github.com/zerodotfive/matrix-webhook/compare/v1.0.0...v2.0.0
[v1.0.0]: https://github.com/zerodotfive/matrix-webhook/releases/tag/v1.0.0
