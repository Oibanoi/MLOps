from typing import List

from fastapi import APIRouter, Path

from API.schemas.sche_request import Request

router = APIRouter()


@router.post('/{phaseid}/{probid}/predict')
def predict(data: Request, phaseid: str = Path(..., title=""), probid: str = Path(..., title="")):
    return {'phase_id': phaseid, 'prob_id': probid,'data': data, 'result': 'OK'}
