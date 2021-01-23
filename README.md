# ChainlinkBalanceMonitor

Monitor your Chainlink nodes Ethereum balance on the primary and emergency funding addresses. Results print to console as well as get saved as timeseries JSON files for ingesting into your favorite SIEM/Metrics software.

Build with Docker 

docker build -t chainlinkbalancemonitor .

Sample .env file

PROVIDER=https://mainnet.infura.io/v3/52929....
CHAINLINK_NODE_ADDRESS=0xA8317D47....
CHAINLINK_NODE_EF_ADDRESS=0x4C7DDEd...

