from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer

from opencompass.datasets.livemathbench import LiveMathBenchDataset, LiveMathBenchEvaluator


livemathbench_dataset = dict(
    type=LiveMathBenchDataset,
    path='opencompass/LiveMathBench202412',
    k=16,
    n=48,
    dataset_splits=['202412_CNMO', '202412_CCEE', '202412_AMC', '202412_WLPMC'],
    dataset_languages=['cn', 'en'],
    cot=True,
    version='202412',
    abbr='LiveMathBench-v202412',
    reader_cfg=dict(
        input_columns=['prompt'], 
        output_column='answer'
    ),
    infer_cfg=dict(
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                round=[
                    dict(role='HUMAN', prompt='{prompt}'),
                ]
            )
        ),
        retriever=dict(type=ZeroRetriever),
        inferencer=dict(
            type=GenInferencer, 
            max_out_len=8192
        ),
    ),
    eval_cfg=dict(
        evaluator=dict(
            type=LiveMathBenchEvaluator,
            model_name='',
            url=[]
        )
    )
)
livemathbench_datasets = [livemathbench_dataset]
