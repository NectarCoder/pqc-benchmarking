#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import other py files
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from csv_builder import init_benchmarks_csv, add_benchmarks  # type: ignore
from calculate_averages import calculate_averages, calculate_medians  # type: ignore

def run_benchmark(out_csv, prefix, static_items, runs=1):
    print(f"\n\033[93mBenchmarking {static_items[1]}...\033[0m")
    avg_kp, avg_csr, avg_cert, avg_ver = calculate_averages(prefix, runs=runs)
    med_kp, med_csr, med_cert, med_ver = calculate_medians(prefix, runs=runs)
    add_benchmarks(
        out_csv,
        static_items,
        [avg_kp, avg_csr, avg_cert, avg_ver],
        [med_kp, med_csr, med_cert, med_ver]
    )
    print(f"\n\033[92m{static_items[1]} Benchmarking Complete. See metrics below:\033[0m")
    print("Metrics Order: [CPU Cycles, Real time, CPU time, Memory/Peak RSS]")
    for label, avg, med in [
        ("Keypair", avg_kp, med_kp),
        ("CSR",     avg_csr, med_csr),
        ("Cert",    avg_cert, med_cert),
        ("Verify",  avg_ver, med_ver),
    ]:
        print(f"{static_items[1]} Average {label} Metrics: {avg}")
        print(f"{static_items[1]} Median  {label} Metrics: {med}")

if __name__ == "__main__":

    # Set path for benchmarks file.
    out_csv = os.path.join(os.path.dirname(__file__), 'results', 'benchmarks.csv')

    # Create the CSV file
    init_benchmarks_csv(out_csv=out_csv)

    """ BENCHMARKING PROCESS BEGINS """
    print("\n\033[92mStarting benchmarking process...\033[0m")

    # Run benchmarks for each algorithm
    # Arguments: (output_csv, prefix, [algorithm id, algorithm name, NIST security level, private key size, public key size, signature size])
    # run_benchmark(out_csv, 'rsa',        ['rsa', 'RSA 2048', 'N/A','1191','294','256'])
    # run_benchmark(out_csv, 'dilithium2', ['mldsa44','Dilithium 2', '2','2626','1334','2420'])
    # run_benchmark(out_csv, 'dilithium3', ['mldsa65','Dilithium 3', '3','4098','1974','3309'])
    # run_benchmark(out_csv, 'dilithium5', ['mldsa87','Dilithium 5', '5','4962','2614','4627'])
    # run_benchmark(out_csv, 'sphincssha1s', ['slh-dsa-sha2-128s','SPHINCS+ SHA 128s', '1','84','50','7856'])
    # run_benchmark(out_csv, 'sphincssha3s', ['slh-dsa-sha2-192s','SPHINCS+ SHA 192s', '3','116','66','16224'])
    # run_benchmark(out_csv, 'sphincssha5s', ['slh-dsa-sha2-256s','SPHINCS+ SHA 256s', '5','150','82','29792'])
    # run_benchmark(out_csv, 'sphincsshake1s', ['slh-dsa-shake-128s','SPHINCS+ SHAKE 128s', '1','84','50','7856'])
    # run_benchmark(out_csv, 'sphincsshake3s', ['slh-dsa-shake-192s','SPHINCS+ SHAKE 192s', '3','116','66','16224'])
    # run_benchmark(out_csv, 'sphincsshake5s', ['slh-dsa-shake-256s','SPHINCS+ SHAKE 256s', '5','150','82','29792'])
    # run_benchmark(out_csv, 'falcon512', ['falcon512','FALCON 512','1','2202','915','657'])
    # run_benchmark(out_csv, 'falcon1024', ['falcon1024','FALCON 1024','5','4122','1811','1267'])
    # run_benchmark(out_csv, 'mayo1', ['mayo1','MAYO 1','1','1469','1439','454'])
    # run_benchmark(out_csv, 'mayo2', ['mayo2','MAYO 2','2','4961','4931','186'])
    # run_benchmark(out_csv, 'mayo3', ['mayo3','MAYO 3','3','3043','3005','681'])
    # run_benchmark(out_csv, 'mayo5', ['mayo5','MAYO 5','5','5619','5573','964'])
    # run_benchmark(out_csv, 'crossrsdp1s', ['CROSS-RSDP-128-small','CROSS-RSDP-128-Small','1','136','99','12432'])
    # run_benchmark(out_csv, 'crossrsdp3s', ['CROSS-RSDP-192-small','CROSS-RSDP-192-Small','3','192','138','28391'])
    # run_benchmark(out_csv, 'crossrsdp5s', ['CROSS-RSDP-256-small','CROSS-RSDP-256-Small','5','246','177','50818'])
    # run_benchmark(out_csv, 'crossrsdpg1s', ['CROSS-RSDP-G-128-small','CROSS-RSDP-G-128-Small','1','112','76','8960'])
    # run_benchmark(out_csv, 'crossrsdpg3s', ['CROSS-RSDP-G-192-small','CROSS-RSDP-G-192-Small','3','160','105','20452'])
    # run_benchmark(out_csv, 'crossrsdpg5s', ['CROSS-RSDP-G-256-small','CROSS-RSDP-G-256-Small','5','199','128','36454'])
    # run_benchmark(out_csv, 'snova2454', ['snova2454','SNOVA_24_5_4','1','1089','1035','248'])
    # run_benchmark(out_csv, 'snova37172', ['snova37172','SNOVA_37_17_2','1','9915','9861','124'])
    # run_benchmark(out_csv, 'snova2583', ['snova2583','SNOVA_25_8_3','3','2393','2339','165'])
    # run_benchmark(out_csv, 'snova56252', ['snova56252','SNOVA_56_25_2','3','31339','31285','178'])
    # run_benchmark(out_csv, 'snova2455', ['snova2455','SNOVA_24_5_5','3','1652','1598','379'])
    # run_benchmark(out_csv, 'snova49113', ['snova49113','SNOVA_49_11_3','5','6079','6025','286'])
    # run_benchmark(out_csv, 'snova3784', ['snova3784','SNOVA_37_8_4','5','4185','4131','376'])
    # run_benchmark(out_csv, 'snova60104', ['snova60104','SNOVA_60_10_4','5','8089','8035','576'])
    # run_benchmark(out_csv, 'snova2965', ['snova2965','SNOVA_29_6_5','5','2789','2735','454'])
    # run_benchmark(out_csv, 'uovis', ['OV_Is', 'UOV-Is', '1', '760892', '412181', '96'])
    # run_benchmark(out_csv, 'uovip', ['OV_Ip', 'UOV-Ip', '1', '516356', '278453', '128'])
    # run_benchmark(out_csv, 'uoviii', ['OV_III', 'UOV-III', '3', '2269788', '1225461', '200'])
    # run_benchmark(out_csv, 'uovv', ['OV_V', 'UOV-V', '5', '5306172', '2869461', '260'])

    run_benchmark(out_csv, 'perk128fast3', ['perk128fast3','PERK 128 Fast 3 Iterations','1','164','148','8345'])
    run_benchmark(out_csv, 'perk128short3', ['perk128short3','PERK 128 Short 3 Iterations','1','164','148','6251'])

    run_benchmark(out_csv, 'hawk512', ['hawk512','HAWK 512','1','184','1024','555'])
    run_benchmark(out_csv, 'hawk1024', ['hawk1024','HAWK 1024','5','360','2440','1221'])


    # We are not testing the "fast" variants of SPHINCS+
    # run_benchmark(out_csv, 'sphincssha1f', ['slh-dsa-sha2-128f','SPHINCS+ SHA 128f', '1','84','50','17088'])
    # run_benchmark(out_csv, 'sphincssha3f', ['slh-dsa-sha2-192f','SPHINCS+ SHA 192f', '3','116','66','35664'])
    # run_benchmark(out_csv, 'sphincssha5f', ['slh-dsa-sha2-256f','SPHINCS+ SHA 256f', '5','150','82','49856'])
    # run_benchmark(out_csv, 'sphincsshake1f', ['slh-dsa-shake-128f','SPHINCS+ SHAKE 128f', '1','84','50','17088'])
    # run_benchmark(out_csv, 'sphincsshake3f', ['slh-dsa-shake-192f','SPHINCS+ SHAKE 192f', '3','116','66','35664'])
    # run_benchmark(out_csv, 'sphincsshake5f', ['slh-dsa-shake-256f','SPHINCS+ SHAKE 256f', '5','150','82','49856'])
