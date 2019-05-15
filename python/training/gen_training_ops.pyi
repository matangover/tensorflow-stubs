# Stubs for tensorflow.python.training.gen_training_ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any as Any, Optional as Optional

def apply_ada_max(var: Any, m: Any, v: Any, beta1_power: Any, lr: Any, beta1: Any, beta2: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_adadelta(var: Any, accum: Any, accum_update: Any, lr: Any, rho: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_adagrad(var: Any, accum: Any, lr: Any, grad: Any, use_locking: bool = ..., update_slots: bool = ..., name: Optional[Any] = ...): ...
def apply_adagrad_da(var: Any, gradient_accumulator: Any, gradient_squared_accumulator: Any, grad: Any, lr: Any, l1: Any, l2: Any, global_step: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_adam(var: Any, m: Any, v: Any, beta1_power: Any, beta2_power: Any, lr: Any, beta1: Any, beta2: Any, epsilon: Any, grad: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ...): ...
def apply_add_sign(var: Any, m: Any, lr: Any, alpha: Any, sign_decay: Any, beta: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_centered_rms_prop(var: Any, mg: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_ftrl(var: Any, accum: Any, linear: Any, grad: Any, lr: Any, l1: Any, l2: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_ftrl_v2(var: Any, accum: Any, linear: Any, grad: Any, lr: Any, l1: Any, l2: Any, l2_shrinkage: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_gradient_descent(var: Any, alpha: Any, delta: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_momentum(var: Any, accum: Any, lr: Any, grad: Any, momentum: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ...): ...
def apply_power_sign(var: Any, m: Any, lr: Any, logbase: Any, sign_decay: Any, beta: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_proximal_adagrad(var: Any, accum: Any, lr: Any, l1: Any, l2: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_proximal_gradient_descent(var: Any, alpha: Any, l1: Any, l2: Any, delta: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def apply_rms_prop(var: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_ada_max(var: Any, m: Any, v: Any, beta1_power: Any, lr: Any, beta1: Any, beta2: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_ada_max_eager_fallback(var: Any, m: Any, v: Any, beta1_power: Any, lr: Any, beta1: Any, beta2: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_adadelta(var: Any, accum: Any, accum_update: Any, lr: Any, rho: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_adadelta_eager_fallback(var: Any, accum: Any, accum_update: Any, lr: Any, rho: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_adagrad(var: Any, accum: Any, lr: Any, grad: Any, use_locking: bool = ..., update_slots: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_adagrad_eager_fallback(var: Any, accum: Any, lr: Any, grad: Any, use_locking: bool = ..., update_slots: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_adagrad_da(var: Any, gradient_accumulator: Any, gradient_squared_accumulator: Any, grad: Any, lr: Any, l1: Any, l2: Any, global_step: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_adagrad_da_eager_fallback(var: Any, gradient_accumulator: Any, gradient_squared_accumulator: Any, grad: Any, lr: Any, l1: Any, l2: Any, global_step: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_adam(var: Any, m: Any, v: Any, beta1_power: Any, beta2_power: Any, lr: Any, beta1: Any, beta2: Any, epsilon: Any, grad: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_adam_eager_fallback(var: Any, m: Any, v: Any, beta1_power: Any, beta2_power: Any, lr: Any, beta1: Any, beta2: Any, epsilon: Any, grad: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_add_sign(var: Any, m: Any, lr: Any, alpha: Any, sign_decay: Any, beta: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_add_sign_eager_fallback(var: Any, m: Any, lr: Any, alpha: Any, sign_decay: Any, beta: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_centered_rms_prop(var: Any, mg: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_centered_rms_prop_eager_fallback(var: Any, mg: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_ftrl(var: Any, accum: Any, linear: Any, grad: Any, lr: Any, l1: Any, l2: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_ftrl_eager_fallback(var: Any, accum: Any, linear: Any, grad: Any, lr: Any, l1: Any, l2: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_ftrl_v2(var: Any, accum: Any, linear: Any, grad: Any, lr: Any, l1: Any, l2: Any, l2_shrinkage: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_ftrl_v2_eager_fallback(var: Any, accum: Any, linear: Any, grad: Any, lr: Any, l1: Any, l2: Any, l2_shrinkage: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_gradient_descent(var: Any, alpha: Any, delta: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_gradient_descent_eager_fallback(var: Any, alpha: Any, delta: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_momentum(var: Any, accum: Any, lr: Any, grad: Any, momentum: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_momentum_eager_fallback(var: Any, accum: Any, lr: Any, grad: Any, momentum: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_power_sign(var: Any, m: Any, lr: Any, logbase: Any, sign_decay: Any, beta: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_power_sign_eager_fallback(var: Any, m: Any, lr: Any, logbase: Any, sign_decay: Any, beta: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_proximal_adagrad(var: Any, accum: Any, lr: Any, l1: Any, l2: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_proximal_adagrad_eager_fallback(var: Any, accum: Any, lr: Any, l1: Any, l2: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_proximal_gradient_descent(var: Any, alpha: Any, l1: Any, l2: Any, delta: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_proximal_gradient_descent_eager_fallback(var: Any, alpha: Any, l1: Any, l2: Any, delta: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_apply_rms_prop(var: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_apply_rms_prop_eager_fallback(var: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_adadelta(var: Any, accum: Any, accum_update: Any, lr: Any, rho: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_adadelta_eager_fallback(var: Any, accum: Any, accum_update: Any, lr: Any, rho: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_adagrad(var: Any, accum: Any, lr: Any, grad: Any, indices: Any, use_locking: bool = ..., update_slots: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_adagrad_eager_fallback(var: Any, accum: Any, lr: Any, grad: Any, indices: Any, use_locking: bool = ..., update_slots: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_adagrad_da(var: Any, gradient_accumulator: Any, gradient_squared_accumulator: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, global_step: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_adagrad_da_eager_fallback(var: Any, gradient_accumulator: Any, gradient_squared_accumulator: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, global_step: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_centered_rms_prop(var: Any, mg: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_centered_rms_prop_eager_fallback(var: Any, mg: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_ftrl(var: Any, accum: Any, linear: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_ftrl_eager_fallback(var: Any, accum: Any, linear: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_ftrl_v2(var: Any, accum: Any, linear: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, l2_shrinkage: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_ftrl_v2_eager_fallback(var: Any, accum: Any, linear: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, l2_shrinkage: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_momentum(var: Any, accum: Any, lr: Any, grad: Any, indices: Any, momentum: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_momentum_eager_fallback(var: Any, accum: Any, lr: Any, grad: Any, indices: Any, momentum: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_proximal_adagrad(var: Any, accum: Any, lr: Any, l1: Any, l2: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_proximal_adagrad_eager_fallback(var: Any, accum: Any, lr: Any, l1: Any, l2: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_proximal_gradient_descent(var: Any, alpha: Any, l1: Any, l2: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_proximal_gradient_descent_eager_fallback(var: Any, alpha: Any, l1: Any, l2: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def resource_sparse_apply_rms_prop(var: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def resource_sparse_apply_rms_prop_eager_fallback(var: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ..., ctx: Optional[Any] = ...): ...
def sparse_apply_adadelta(var: Any, accum: Any, accum_update: Any, lr: Any, rho: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_adagrad(var: Any, accum: Any, lr: Any, grad: Any, indices: Any, use_locking: bool = ..., update_slots: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_adagrad_da(var: Any, gradient_accumulator: Any, gradient_squared_accumulator: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, global_step: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_centered_rms_prop(var: Any, mg: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_ftrl(var: Any, accum: Any, linear: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_ftrl_v2(var: Any, accum: Any, linear: Any, grad: Any, indices: Any, lr: Any, l1: Any, l2: Any, l2_shrinkage: Any, lr_power: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_momentum(var: Any, accum: Any, lr: Any, grad: Any, indices: Any, momentum: Any, use_locking: bool = ..., use_nesterov: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_proximal_adagrad(var: Any, accum: Any, lr: Any, l1: Any, l2: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_proximal_gradient_descent(var: Any, alpha: Any, l1: Any, l2: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...
def sparse_apply_rms_prop(var: Any, ms: Any, mom: Any, lr: Any, rho: Any, momentum: Any, epsilon: Any, grad: Any, indices: Any, use_locking: bool = ..., name: Optional[Any] = ...): ...