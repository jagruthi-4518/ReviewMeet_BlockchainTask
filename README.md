# ReviewMeet_BlockchainTask
## Overview of Elements in The code
1. Hashing
2. Mining and Proof of work
3. Validation and Integration
4. Simulation that allows user to set the difficulty and start the blockchain, add blocks, check validity and check the validation when a block is randomly choosen and tampered

### 1. SHA-256 Hashing
Each block is hashed using the SHA-256 cryptographic hashing algorithm from Python’s `hashlib` library.

The hash is generated from:
- Block data
- Timestamp
- Previous block hash
- Nonce

```python
def hashing(data,timestamp,prevHash,nonce):
    hashInput = str(data)+str(timestamp)+str(prevHash)+str(nonce)
    return hashlib.sha256(hashInput.encode()).hexdigest()
```

This ensures that even a tiny change in block data results in a completely different hash.

### 2. Mining and Proof of Work
Mining is implemented by repeatedly changing a **nonce** value until the hash of the current block satisfies a certain diffuculty(a certain number to start with) and reaches the target. 

```python
 while True:
        hash = hashing(data,timestamp,prevHash,nonce)
        if hash[:difficulty]== target:
            print("Found Nonce:",nonce)
            print("Hash:",hash)

            #returning attributes for the block
            #the block structure is created
            return{
                "index": index,
                "timestamp": timestamp,
                "data": data,
                "prevHash": prevHash,
                "nonce": nonce,
                "hash": hash
            }
        #incrementing the nonce until it reaches the target 
        else:
            nonce+=1
```

Once mined, gives an output like,
![Mining Output](Screenshot%202026-05-16%20194506.png)

And after the Mining is done, the function returns the block structure with its data(index,timestamp ect.) as attributes

### 3.Validation and integrity of the blockchain
 #### 1. for the genesis block:
- Checking if the hash of the block is equal to the calculated
  ```python
  genesis = blockchain[0]
    if genesis["hash"] != hashing(genesis["data"], genesis["timestamp"], genesis["prevHash"], genesis["nonce"]):
        return False
  ```
- Checking if the hash is satisfying the difficuly
    ```python
      if genesis["hash"][:difficulty] != target:
        return False
    ```
#### 2. For other blocks
- Check if the current block hash is matching the calculated hash
```python
 #checking if current block hash is equal to the calculated
        if current_block["hash"] != hashing(current_block["data"],current_block["timestamp"],current_block["prevHash"],current_block["nonce"]):
            return False
```
- Check if the previous block hash in the current block is matching the hash of previous bock
```python
 #checking if previous block has is same as the previous hash in the current block
        if current_block["prevHash"]!=prev_block["hash"]:
            return False
```
- Checking if the current hash is satisfying the difficulty\
```python
#checking the hash actually satisfies the difficulty target
        if current_block["hash"][:difficulty]!= target:
            return False
```
Returns a Boolean
### 4. Initiation of blockchain
The blockchain is initiated but is maintained empty at the begining
```python
blockchain = []
```
### 5. Creating the Genesis Block
The Blockchain begins with a special first block called as genesis block.

**Since it has no previous block, it is manually assigned to be 0.**

The created block is appended to the blockchain
```python
def create_genesis_block(difficulty):
    genesis_block = mining(0,"GenesisBlock","0",difficulty)
    blockchain.append(genesis_block)
```
### 5. Adding a Block
After calling the function `add_block()` the block is mined and is displayed like this on the terminal.

![Mining Output](Screenshot%202026-05-16%20194506.png)

And then the block is appended to the chain
```python
def add_block(blockchain,data,difficulty):
    block=mining(len(blockchain),data,blockchain[-1]["hash"],difficulty)
    blockchain.append(block)
```
## HOW THE SIMULATION WORKS
#### Step-1
The computer asks the user to input the difficulty.
#### Step-2
The `create_genesis_block()` is called and the blockchain is started.
#### Step-3
There is continuos loop that runs until the user wants to exit.

It gives 4 choices:
- Add block
- Validate the block chain
- Tamper a randomly choosen block with a fake data
- Exit the session

### Outputs
1. After inputing the difficulty, the create genesis function is called and it is mined as shown below.
   
   ![Create_genesis Output](Screenshot%202026-05-16%20194529.png)
   
2. #### Chosing option 1 - Add Block

   ![Add_block Output](Screenshot%202026-05-16%20194623.png)
   
After we choose 1 we get to input the data, after entering the block is mined and the whole chain along with all the block attributes is displayed as we can see in the screenshot.

3. #### Choosing option 2- Validation of the block chain

![Validation Output](Screenshot%202026-05-16%20194656.png)

The blockchain as a whole is displayed and at last shows whether the blockchain is valid or not.

4. #### Option 4 - Random tampering and validating the blockchain
   
![Tampering Output_after_data](Screenshot%202026-05-19%20150723.png)

![Tampering Output_before_data](Screenshot%202026-05-19%20150624.png)


It displays no. of the block that has been tampered with.

Displays the blockchain after tampering and we can observe in the displayed data that the transaction is changed to **This Transaction is Tampered**.We can also observe that the hash of the block which was tampered is changed from the above two picture if we compared.

And we can also see that the Blockchain validation shows False in the end showing that if any transaction is tampered with, the successive blocks of the chain break and this is where the validation breaks.





