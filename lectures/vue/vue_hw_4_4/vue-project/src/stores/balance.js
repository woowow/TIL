import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', {
  state: () => ({
    balances: [
      { name: '김하나', balance: 100000 },
      { name: '김두리', balance: 10000 },
      { name: '김서이', balance: 100 }
    ]
  }),
  getters: {
    getByName: (state) => {
      return (name) => state.balances.find(b => b.name === name)
    }
  },
  actions: {
    increaseBalance(name, amount = 1000) {
      const target = this.balances.find(b => b.name === name)
      if (target) target.balance += amount
    }
  }
})
