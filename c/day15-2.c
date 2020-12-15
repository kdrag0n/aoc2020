#include <stdio.h>
#include <stdlib.h>

#define TURNS 30000000

struct num_turn_hist {
    int last;
    int cur;
};

void main() {
    int starts[] = {1,2,16,19,18,0};
    int starts_len = 6;

    int num = -1;
    int last_num = -1;
    unsigned int *num_occurs = calloc(TURNS, sizeof(*num_occurs));
    struct num_turn_hist *num_turns = calloc(TURNS, sizeof(*num_turns));

    for (int turn = 0; turn < TURNS; turn++) {
        if (turn % 1000 == 0) {
            printf("%d\n", turn);
        }

        if (turn < starts_len) {
            num = starts[turn];
        } else if (last_num != -1 && num_occurs[last_num] == 1) {
            num = 0;
        } else {
            int last_spk = num_turns[last_num].cur + 1;
            int last_last_spk = num_turns[last_num].last + 1;
            num = last_spk - last_last_spk;
        }

        last_num = num;
        num_occurs[num]++;
        struct num_turn_hist *hist = &num_turns[num];
        hist->last = hist->cur;
        hist->cur = turn;
    }

    printf("\n%d\n", num);
}
