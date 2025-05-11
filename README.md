# OpenSSL Builds

This repository contains automated builds of OpenSSL for various Linux distributions. The builds are created using GitHub Actions and are optimized for MediaEase applications.

## Supported Versions

- OpenSSL 3.0.15

## Supported Distributions

- Debian 11 (Bullseye)
- Ubuntu 22.04 LTS

## Build Configuration

The OpenSSL packages are built with the following configuration:

```bash
./Configure shared
```

## Usage

### Manual Installation

1. Download the appropriate .deb package for your distribution from the [Releases](https://github.com/MediaEase-binaries/openssl-builds/releases) page
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation

The packages include JSON metadata files that can be used for automated installations. Each package is accompanied by a .json file containing:

- Package information
- Checksums
- Dependencies
- Build configuration
- Distribution details

## License

OpenSSL is distributed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Build Process

The build process is automated using GitHub Actions. The workflow:

1. Sets up the build environment
2. Downloads and installs dependencies
3. Builds OpenSSL from source
4. Creates Debian packages
5. Generates metadata
6. Creates GitHub releases

## Security

These builds are created from official OpenSSL source code. The build process is transparent and reproducible. All packages are signed and include checksums for verification. 
