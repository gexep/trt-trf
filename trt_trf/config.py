from lazycls.envs import Env

"""
Setting some default settings for workspace size

7gb = 7168
8gb = 8192
16g = 16384
24g = 24576
32g = 32768

"""


class TRTWorkspaceConfig:
    default_trt_workspace_mb: int = Env.to_int('DEFAULT_TRT_WORKSPACE_MB', 24576)
    t5_encoder_workspace_mb: int = Env.to_int('T5_ENCODER_TRT_WORKSPACE_MB', 16384)
    t5_decoder_workspace_mb: int = Env.to_int('T5_DECODER_TRT_WORKSPACE_MB', 24576)

    def set_workspace_gb(cls, gb: int = 16):
        """ Sets all the workspaces to gb * 1024"""
        cls.default_trt_workspace_mb = gb * 1024
        cls.t5_encoder_workspace_mb = gb * 1024
        cls.t5_decoder_workspace_mb = gb * 1024
    
    def set_default_workspace_gb(cls, gb: int = 16):
        """ Sets all the default workspaces to gb * 1024"""
        cls.default_trt_workspace_mb = gb * 1024

    def set_t5_workspace_gb(cls, gb: int = 16):
        """ Sets all the t5 workspaces to gb * 1024"""
        cls.t5_encoder_workspace_mb = gb * 1024
        cls.t5_decoder_workspace_mb = gb * 1024



    