# Chat-Room-peer-to-peer-model

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Helper Server](#helper-server)
  - [Peer Clients](#peer-clients)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project implements a peer-to-peer chat room, allowing direct communication between multiple clients. It consists of a chat server and multiple peer clients, specifically Client_01, Client_02, Client_03, and Client_04, that connect directly to each other. Additionally, a helper server is used for peer discovery to facilitate initial connections.

## Features

- True peer-to-peer communication: Clients (Client_01, Client_02, Client_03, and Client_04) connect directly to each other.
- A helper server for peer discovery: Helps clients find each other.
- Real-time, two-way text communication.
- Support for custom usernames.
- Graceful handling of client disconnects.

## Prerequisites

Before using this chat room application, ensure you have the following:

- Python 3.x installed on your machine.
- Basic knowledge of how to run Python scripts.
- Terminal or command prompt to execute the helper server and peer clients.

## Usage

### Helper Server

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the helper server script using the following command:

   ```bash
   python helper_server.py
   ```

4. The helper server will start and listen on a specified port for peer discovery requests (default: 12345).

### Peer Clients

1. Open a new terminal or command prompt for each peer client instance, such as Client_01, Client_02, etc.
2. Navigate to the project directory.
3. Run the peer client script for each specific client instance using the following command:

   ```bash
   python Client_01.py
   ```

4. Follow the on-screen prompts to enter a username, the helper server's IP address, and port.

5. The peer client instances will connect to the helper server to discover peers and initiate direct connections for messaging.

## Example

Here's an example of how to run the chat room:

1. Start the helper server on a terminal:

   ```bash
   python helper_server.py
   ```

2. Start multiple peer client instances (Client_01, Client_02, Client_03, and Client_04) in separate terminals:

   ```bash
   python Client_01.py
   ```

3. Connect each peer client to the helper server by providing the server's IP address and port.

4. The helper server will help peer clients (Client_01, Client_02, Client_03, and Client_04) discover each other, and you can start sending messages directly between them.

## Contributing

We welcome contributions to this project! You can contribute by opening issues, submitting pull requests, or suggesting new features to enhance the peer-to-peer chat room.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: This is a peer-to-peer chat room example, and additional security and scalability measures may be needed for production use.*
