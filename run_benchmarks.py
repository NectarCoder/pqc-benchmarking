#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import other py files
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from csv_builder import init_benchmarks_csv, add_benchmarks  # type: ignore
from calculate_averages import calculate_averages, calculate_medians  # type: ignore

def run_benchmark(out_csv, prefix, static_items, runs=1): # Needs to be changed to runs=1000
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

    # DONE
    # run_benchmark(out_csv, 'rsa',        ['rsa', 'RSA 2048', 'N/A','1190','294','256'])

    # DONE
    # run_benchmark(out_csv, 'dilithium2', ['mldsa44','ML-DSA/Dilithium 2', '2','2560','1312','2420'])
    # run_benchmark(out_csv, 'dilithium3', ['mldsa65','ML-DSA/Dilithium 3', '3','4032','1952','3309'])
    # run_benchmark(out_csv, 'dilithium5', ['mldsa87','ML-DSA/Dilithium 5', '5','4896','2592','4627'])

    # NOT DONE
    # run_benchmark(out_csv, 'sphincssha1s', ['slh-dsa-sha2-128s','SLH-DSA/SPHINCS+ SHA 128s', '1','64','32','7856'])
    # run_benchmark(out_csv, 'sphincssha3s', ['slh-dsa-sha2-192s','SLH-DSA/SPHINCS+ SHA 192s', '3','96','48','16224'])
    # run_benchmark(out_csv, 'sphincssha5s', ['slh-dsa-sha2-256s','SLH-DSA/SPHINCS+ SHA 256s', '5','128','64','29792'])
    # run_benchmark(out_csv, 'sphincsshake1s', ['slh-dsa-shake-128s','SLH-DSA/SPHINCS+ SHAKE 128s', '1','64','32','7856'])
    # run_benchmark(out_csv, 'sphincsshake3s', ['slh-dsa-shake-192s','SLH-DSA/SPHINCS+ SHAKE 192s', '3','96','48','16224'])
    # run_benchmark(out_csv, 'sphincsshake5s', ['slh-dsa-shake-256s','SLH-DSA/SPHINCS+ SHAKE 256s', '5','128','64','29792'])

    # DONE
    # run_benchmark(out_csv, 'falcon512', ['falcon512','FALCON 512','1','1281','897','666'])
    # run_benchmark(out_csv, 'falcon1024', ['falcon1024','FALCON 1024','5','2305','1793','1280'])

    # DONE
    # run_benchmark(out_csv, 'mayo1', ['mayo1','MAYO 1','1','24','1420','454'])
    # run_benchmark(out_csv, 'mayo2', ['mayo2','MAYO 2','1','24','4912','186'])
    # run_benchmark(out_csv, 'mayo3', ['mayo3','MAYO 3','3','32','2986','681'])
    # run_benchmark(out_csv, 'mayo5', ['mayo5','MAYO 5','5','40','5554','964'])

    # NOT DONE
    # run_benchmark(out_csv, 'crossrsdp1s', ['CROSSrsdp128small','CROSS-RSDP-128-Small','1','32','77','12432'])
    # run_benchmark(out_csv, 'crossrsdp3s', ['CROSSrsdp192small','CROSS-RSDP-192-Small','3','48','115','28391'])
    # run_benchmark(out_csv, 'crossrsdp5s', ['CROSSrsdp256small','CROSS-RSDP-256-Small','5','64','153','50818'])
    # run_benchmark(out_csv, 'crossrsdpg1s', ['CROSSrsdpg128small','CROSS-RSDP-G-128-Small','1','32','54','8960'])
    # run_benchmark(out_csv, 'crossrsdpg3s', ['CROSSrsdpg192small','CROSS-RSDP-G-192-Small','3','48','83','20452'])
    # run_benchmark(out_csv, 'crossrsdpg5s', ['CROSSrsdpg256small','CROSS-RSDP-G-256-Small','5','64','106','36454'])

    # DONE
    # run_benchmark(out_csv, 'snova2454', ['snova2454','SNOVA-24-5-4','1','48','1016','248'])
    # run_benchmark(out_csv, 'snova37172', ['snova37172','SNOVA-37-17-2','1','48','9842','124'])
    # run_benchmark(out_csv, 'snova2583', ['snova2583','SNOVA-25-8-3','1','48','2320','165'])
    # run_benchmark(out_csv, 'snova56252', ['snova56252','SNOVA-56-25-2','3','48','31266','178'])
    # run_benchmark(out_csv, 'snova49113', ['snova49113','SNOVA-49-11-3','3','48','6006','286'])
    # run_benchmark(out_csv, 'snova3784', ['snova3784','SNOVA-37-8-4','3','48','4112','376'])
    # run_benchmark(out_csv, 'snova2455', ['snova2455','SNOVA-24-5-5','3','48','1579','379'])
    # run_benchmark(out_csv, 'snova60104', ['snova60104','SNOVA-60-10-4','5','48','8016','576'])
    # run_benchmark(out_csv, 'snova2965', ['snova2965','SNOVA-29-6-5','5','48','2716','454'])
    # run_benchmark(out_csv, 'snova66153', ['snova66153','SNOVA-66-15-3','5','48','15204','381'])
    # run_benchmark(out_csv, 'snova75332', ['snova75332','SNOVA-75-33-2','5','48','71890','232'])

    # DONE
    # run_benchmark(out_csv, 'uovis', ['OV_Is', 'UOV-Is', '1', '760892', '412181', '96'])
    # run_benchmark(out_csv, 'uovip', ['OV_Ip', 'UOV-Ip', '1', '516356', '278453', '128'])
    # run_benchmark(out_csv, 'uoviii', ['OV_III', 'UOV-III', '3', '2269788', '1225461', '200'])
    # run_benchmark(out_csv, 'uovv', ['OV_V', 'UOV-V', '5', '5306172', '2869461', '260'])

    # DONE
    # run_benchmark(out_csv, 'hawk512', ['hawk512','HAWK 512','1','184','1024','555'])
    # run_benchmark(out_csv, 'hawk1024', ['hawk1024','HAWK 1024','5','360','2440','1221'])
    
    # NOT DONE
    # run_benchmark(out_csv, 'faest128s', ['faest128s','FAEST 128s','1','32','32','4506'])
    # run_benchmark(out_csv, 'faest192s', ['faest192s','FAEST 192s','3','40','48','11260'])
    # run_benchmark(out_csv, 'faest256s', ['faest256s','FAEST 256s','5','48','48','20696'])
    # run_benchmark(out_csv, 'faestem128s', ['faestem128s','FAEST-EM 128s','1','32','32','3906'])
    # run_benchmark(out_csv, 'faestem192s', ['faestem192s','FAEST-EM 192s','3','48','48','9340'])
    # run_benchmark(out_csv, 'faestem256s', ['faestem256s','FAEST-EM 256s','5','64','64','17984'])

    # NOT DONE
    # run_benchmark(out_csv, 'perkak1short', ['perkak1short','PERK-AES-KECCAK-1-short','1','120','104','3473'])
    # run_benchmark(out_csv, 'perkak3short', ['perkak3short','PERK-AES-KECCAK-3-short','3','175','151','8311'])
    # run_benchmark(out_csv, 'perkak5short', ['perkak5short','PERK-AES-KECCAK-5-short','5','227','195','14830'])

    # NOT DONE
    # run_benchmark(out_csv, 'ryde1s', ['ryde1s','RYDE 1-Short','1','32','69','3115'])
    # run_benchmark(out_csv, 'ryde3s', ['ryde3s','RYDE 3-Short','3','48','101','7064'])
    # run_benchmark(out_csv, 'ryde5s', ['ryde5s','RYDE 5-Short','5','64','132','12607'])
    
    # NOT DONE
    # run_benchmark(out_csv, 'mirath1ashort', ['mirathtcith1ashort','MIRATH-TCITH-1a-Short','1','32','73','3182'])
    # run_benchmark(out_csv, 'mirath1bshort', ['mirathtcith1bshort','MIRATH-TCITH-1b-Short','1','32','57','2990'])
    # run_benchmark(out_csv, 'mirath3ashort', ['mirathtcith3ashort','MIRATH-TCITH-3a-Short','3','48','107','7456'])
    # run_benchmark(out_csv, 'mirath3bshort', ['mirathtcith3bshort','MIRATH-TCITH-3b-Short','3','48','84','6825'])
    # run_benchmark(out_csv, 'mirath5ashort', ['mirathtcith5ashort','MIRATH-TCITH-5a-Short','5','64','147','13091'])
    # run_benchmark(out_csv, 'mirath5bshort', ['mirathtcith5bshort','MIRATH-TCITH-5b-Short','5','64','112','12229'])

    # NOT DONE
    run_benchmark(out_csv, 'sdithcat1short', ['sdithcat1short','SDitH-CAT-1-Short','1','163','70','3705'])
    run_benchmark(out_csv, 'sdithcat3short', ['sdithcat3short','SDitH-CAT-3-Short','3','232','98','7964'])
    run_benchmark(out_csv, 'sdithcat5short', ['sdithcat5short','SDitH-CAT-5-Short','5','307','132','14121'])

    print("\n\033[92mBenchmarking process complete. Results saved to 'results/benchmarks.csv'.\033[0m")
    
    # We are not testing the "fast" variants of SPHINCS+
    # run_benchmark(out_csv, 'sphincssha1f', ['slh-dsa-sha2-128f','SPHINCS+ SHA 128f', '1','84','50','17088'])
    # run_benchmark(out_csv, 'sphincssha3f', ['slh-dsa-sha2-192f','SPHINCS+ SHA 192f', '3','116','66','35664'])
    # run_benchmark(out_csv, 'sphincssha5f', ['slh-dsa-sha2-256f','SPHINCS+ SHA 256f', '5','150','82','49856'])
    # run_benchmark(out_csv, 'sphincsshake1f', ['slh-dsa-shake-128f','SPHINCS+ SHAKE 128f', '1','84','50','17088'])
    # run_benchmark(out_csv, 'sphincsshake3f', ['slh-dsa-shake-192f','SPHINCS+ SHAKE 192f', '3','116','66','35664'])
    # run_benchmark(out_csv, 'sphincsshake5f', ['slh-dsa-shake-256f','SPHINCS+ SHAKE 256f', '5','150','82','49856'])

    # We are not testing the "fast" variants of PERK (will not work if uncommented)
    # run_benchmark(out_csv, 'perk128fast3', ['perk128fast3','PERK 128 Fast 3 Iterations','1','164','148','8345'])

    # We are not testing the "fast" variants of RYDE (will not work if uncommented)
    # run_benchmark(out_csv, 'ryde1f', ['ryde1f','RYDE 1-Fast','1','32','69','3597'])

    # We are not testing these depreceated versions of perk (these will not work if uncommented)
    # run_benchmark(out_csv, 'perk128short3', ['perk128short3','PERK 128 Short 3 Iterations','1','164','148','6251'])
    # run_benchmark(out_csv, 'perk128short5', ['perk128short5','PERK 128 Short 5 Iterations','5','257','241','5780'])
    # run_benchmark(out_csv, 'perk192short3', ['perk192short3','PERK 192 Short 3 Iterations','3','251','227','14280'])
    # run_benchmark(out_csv, 'perk192short5', ['perk192short5','PERK 192 Short 5 Iterations','5','392','368','13164'])
    # run_benchmark(out_csv, 'perk256short3', ['perk256short3','PERK 256 Short 3 Iterations','3','346','314','25141'])
    # run_benchmark(out_csv, 'perk256short5', ['perk256short5','PERK 256 Short 5 Iterations','5','539','507','23040'])
