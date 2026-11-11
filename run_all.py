"""Run all examples independently and save machine-readable execution evidence."""
from pathlib import Path
import argparse,concurrent.futures,json,os,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
def execute(record):
    start=time.monotonic();env=os.environ.copy()
    env.update(MPLBACKEND='Agg',PYTHONHASHSEED='42',PYTHONIOENCODING='utf-8',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
    try:
        p=subprocess.run([sys.executable,str(ROOT/record['file'])],cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=300)
        result=dict(file=record['file'],passed=p.returncode==0,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr)
    except subprocess.TimeoutExpired:
        result=dict(file=record['file'],passed=False,returncode=None,stdout='',stderr='Timed out after 300 seconds')
    result['seconds']=round(time.monotonic()-start,3)
    return result
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--jobs',type=int,default=2);parser.add_argument('--chapter',type=int);args=parser.parse_args()
    records=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    if args.chapter:records=[r for r in records if r['chapter']==args.chapter]
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for result in pool.map(execute,records):
            results.append(result);print(('PASS ' if result['passed'] else 'FAIL ')+result['file'],flush=True)
    out=ROOT/'validation';out.mkdir(exist_ok=True)
    target=out/(f'chapter_{args.chapter:02}.json' if args.chapter else 'execution-results.json')
    target.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{sum(r["passed"] for r in results)}/{len(results)} passed')
    return 0 if all(r['passed'] for r in results) else 1
if __name__=='__main__':raise SystemExit(main())
