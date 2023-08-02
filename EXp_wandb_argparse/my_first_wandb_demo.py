import wandb
import random

wandb.login()
lr=0.01
epochs=10
run=wandb.init(
	project="my_demo1",
	config={
	"learning_rate": lr,
    	"epochs": epochs,
})

offset=random.random()/5
print(f"lr: {lr}")

for epoch in range(2, epochs):
    acc = 1 - 2 ** -epoch - random.random() / epoch - offset
    loss = 2 ** -epoch + random.random() / epoch + offset
    print(f"epoch={epoch},accuracy:{acc},loss:{loss}")
    # log metrics to wandb
    wandb.log({"acc": acc, "loss": loss})
    
# [optional] finish the wandb run, necessary in notebooks
wandb.finish()

