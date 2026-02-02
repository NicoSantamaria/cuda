#include <cuda_runtime.h>
#include <stdio.h>

int main() {
  int deviceCount = 0;
  cudaGetDeviceCount(&deviceCount);
  printf("CUDA devices found: %d\n", deviceCount);
  return 0;
}