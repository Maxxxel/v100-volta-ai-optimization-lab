#ifndef LLAMA_GRAMMAR_PREFILL_H
#define LLAMA_GRAMMAR_PREFILL_H

#include "llama.h"

#ifdef __cplusplus
extern "C" {
#endif

// Experimental lab API: character-grammar prefill without token normalization.
// Returns false without consuming input for unsupported samplers or token rules.
LLAMA_API bool llama_sampler_accept_grammar_prefill(
        struct llama_sampler * sampler,
                  const char * text,
                        size_t size);

#ifdef __cplusplus
}
#endif

#endif
