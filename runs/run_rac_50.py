import os

# Edit value of num_runs to change the number of repeat runs
num_runs = 1
for i in range(1, num_runs + 1):
    print(f"Starting run No. {i} of {num_runs}")
    
    cmd = (
        "python main.py "
        "--model RACReader "
        "--vocab ./data/mimic3/vocab_rac.csv "
        "--decoder CodeTitle "
        "--Y 50 "
        "--data_path ./data/mimic3/train_50.csv "
        "--MAX_LENGTH 4096 "
        "--embed_file ./data/mimic3/processed_full_300.embed "
        "--tune_wordemb "
        "--batch_size 16 "
        "--lr 8e-5 "
        "--criterion prec_at_8 "
        "--random_seed 0 "
        "--num_workers 1 "
        "--filter_size 9 "
        "--dropout 0.1 "
    )

    os.system(cmd)

print(f"Completed all {num_runs} runs")