from birdman import Multinomial, NegativeBinomial, NegativeBinomialLME
import os
import biom
import pandas as pd
from dask_jobqueue import SLURMCluster
from dask.distributed import Client


TBL_FILE = os.path.join('data', "macaque_tbl.biom")
MD_FILE = os.path.join('data', "macaque_metadata.tsv")

table_biom = biom.load_table(TBL_FILE)
metadata = pd.read_csv(
    MD_FILE,
    sep="\t",
    index_col=0,
)
metadata.index = metadata.index.astype(str)


nb = NegativeBinomial(
    table=table_biom,
    formula="host_common_name",
    metadata=metadata,
    chains=4,
    seed=42,
    beta_prior=2.0,
    cauchy_scale=2.0,
    parallelize_across="features"
)
cluster = SLURMCluster(
    cores=2, processes=2, memory='10GB', walltime='01:00:00',
    interface='ib0', nanny=True, death_timeout='300s',
    # the local directory is **important**
    # make sure it can handle many fast writes
    # see https://github.com/dask/dask-jobqueue/issues/448
    local_directory='/scratch',
    shebang='#!/usr/bin/env bash',
    env_extra=["export TBB_CXX_TYPE=gcc"],
    queue='ccb')

# print(cluster.job_script())
# cluster.scale(jobs=2)
# client = Client(cluster)
# client.wait_for_workers(args.nodes)
# print(cluster.scheduler.workers)
# time.sleep(60)
# print(cluster.scheduler.workers)

nb.compile_model()
print(type(cluster))
nb.fit_model(dask_cluster=cluster)
