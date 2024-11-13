# MLOPS-Prjoect-2
This repository contains all the files used for the second Project of MLOPS at HSLU 2024/25
The project aims to train a model with the given Hyperparameters "learning rate" (default=0.0001), "warmup steps" (default=0), "weight decay" (default=0.0), "batch size" (default=64) and "checkpoint dir" (default="models").

Steps to properly run the project:<br>
-Build a image from the path where the docker file is in by using: docker build -t your_image_name .<br>
-Choose your hyperparameters you want to give the model<br>
-Run the image with your selected hyperparameters by using:<br>
docker run -v your_save_path:/app/your_checkpoint_dir -it your_image_name --learning_rate your_learning_rate --warmup_steps your_warmup_steps --weight_decay your_weight_decay --batch_size your_batch_size --checkpoint_dir your_checkpoint_dir<br>
or alternatively:<br>
docker run -v your_save_path:/app/your_checkpoint_dir -it your_image_name python app/main.py -lr your_learning_rate -ws your_warmup_steps -wd your_weight_decay -bs your_batch_size --checkpoint_dir your_checkpoint_dir<br>
-After the complete run the models state_dict will be saved in your_checkpoint_dir
