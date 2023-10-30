import torch

def hvp(y,w,v):
    '''
    y the output of loss function
    w the parameters of hessian matrix
    v the vector needs product
    '''
    if len(w)!=len(v):
        raise (ValueError("w and v must have the same length"))
    for i,v_ele in enumerate(v):
        v[i]=v_ele.cuda()
    first_grad=torch.autograd.grad(y,w,retain_graph=True,create_graph=True)
    #grad_outputs will weight the calculated gradient
    return_grads=torch.autograd.grad(first_grad,w,grad_outputs=v)
    return return_grads
