## Requests

### `/controls`

| Request URL          | Action             |
|----------------------|--------------------|
| `/controls/left`     | Turn car left      |
| `/controls/right`    | Turn car right     |
| `/controls/forward`  | Move car forward   |
| `/controls/backward` | Move card backward |
| `/controls/stop`     | Stop the car       |

### `/data`

| Request URL      | Action                                                    |
|------------------|-----------------------------------------------------------|
| `/data/ip`       | Get the Pi's IP address                                   |
| `/data/distance` | Get a distance reading (in cm) from the ultrasonic sensor |

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