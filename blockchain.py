import hashlib#for hashing
import time#for timestamps
import random#for randomly picking a number for tampering

#SHA 256 hashing
def hashing(data,timestamp,prevHash,nonce):
    hashInput = str(data)+str(timestamp)+str(prevHash)+str(nonce)
    return hashlib.sha256(hashInput.encode()).hexdigest()

#mining and Proof of Work
def mining(index,data,prevHash,difficulty):
    nonce=0
    timestamp=time.time()
    target = "0"*difficulty#generally difficulty conditons are like hashes starting with some fixed number of 0's
    print("\nMining block",index)
    #running loop until the hash reaches the target
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

#valition of the blockchain
#returns a BOoolean
def validation(blockchain,difficulty):
    target = "0"*difficulty

    #for starting block because it does not have any prev block
    genesis = blockchain[0]
    if genesis["hash"] != hashing(genesis["data"], genesis["timestamp"], genesis["prevHash"], genesis["nonce"]):
        return False
    if genesis["hash"][:difficulty] != target:
        return False
    
    #for rest all blocks because prev_block= blockchain[i-1] breaks if i took range from 0
    for i in range(1,len(blockchain)):
        current_block = blockchain[i]
        prev_block = blockchain[i-1]

        #checking if current block hash is equal to the calculated
        if current_block["hash"] != hashing(current_block["data"],current_block["timestamp"],current_block["prevHash"],current_block["nonce"]):
            return False
        
        #checking if previous block has is same as the previous hash in the current block
        if current_block["prevHash"]!=prev_block["hash"]:
            return False
        
        #checking the hash actually satisfies the difficulty target
        if current_block["hash"][:difficulty]!= target:
            return False
        
    return True


blockchain = []
#the starting block
def create_genesis_block(difficulty):
    genesis_block = mining(0,"GenesisBlock","0",difficulty)
    blockchain.append(genesis_block)

#to add blocks
def add_block(blockchain,data,difficulty):
    block=mining(len(blockchain),data,blockchain[-1]["hash"],difficulty)
    blockchain.append(block)
#displaying the whole block chain
def display_chain(blockchain):
    for block in blockchain:
        print("\n")
        for key, value in block.items():
            print(f"{key}: {value}")


#Simulation
difficulty=int(input("enter difficulty condition:"))#taking difficulty as input
create_genesis_block(difficulty)#creating the first block

#giving choice to the user
while True:
    choice = input("\nPress 1 to add block\n"
                    "Press 2 to validate blockchain\n"
                    "Press 3 to tamper with blockchain and validate\n"
                    "Press 4 to exit\n"
                    "Enter choice: \n"
                    )

    if choice == "1":
        num = int(input("\nEnter number of transactions: "))

        transactions = []

        for i in range(num):
            transaction = input(f"Enter transaction {i+1}: ")
            transactions.append(transaction)

        add_block(blockchain, transactions, difficulty)
        display_chain(blockchain)

    elif choice == "2":
        display_chain(blockchain)
        print("\nBlockchain Valid?:", validation(blockchain, difficulty))

    elif choice == "3":

        if len(blockchain)<=1:
            print("Add atlest 1 block before initiating tampering")
        else:   
             block_no = random.randint(1, len(blockchain) - 1)

        block = blockchain[block_no]
        tx_index = random.randint(0, len(block["data"]) - 1)
        block["data"][tx_index] = "Tampered Transaction"

        block["hash"] = hashing(block["data"],block["timestamp"],block["prevHash"],block["nonce"])

        print(f"\nTampered transaction {tx_index} in block {block_no}")

        display_chain(blockchain)

        print("\nBlockchain Valid?:", validation(blockchain, difficulty))

    elif choice == "4":
        print("\nSession Completed\n")
        break

    else:
        print("\nInvalid choice")

        
