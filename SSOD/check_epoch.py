import torch

# 체크포인트 파일 경로
checkpoint_path = '/workspace/efficientteacher/scripts/mula_convertor/efficient-noremove.pt'

# 체크포인트 로드
checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))

# 체크포인트의 키 확인
print("Keys in the checkpoint:", checkpoint.keys())

# 에폭 정보 출력
if 'epoch' in checkpoint:
    print("Epoch in the checkpoint:", checkpoint['epoch'])
else:
    print("No epoch information in the checkpoint.")