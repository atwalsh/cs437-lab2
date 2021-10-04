## Requests

### `/controls`

| Request URL | Action             |
|-------------|--------------------|
| `/left`     | Turn car left      |
| `/right`    | Turn car right     |
| `/forward`  | Move car forward   |
| `/backward` | Move card backward |
| `/stop`     | Stop the car       |

## Setup
### Install

1. Install Pi-Car dependencies:

    ```console
    sudo python3 setup.py install
    ```

2. Install Python dependencies:

    ```console
    pip3 install -r requirements.txt
    ```

### Run

1. Make sure the Pi-Car hat is turned on
2. Run the Flask app:
   ```console
   python3 app.py
   ```