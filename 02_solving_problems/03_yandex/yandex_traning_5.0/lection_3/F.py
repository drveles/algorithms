import timeit
def main():
    #WA 
    pass

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    print("Time: %s" % (timeit.default_timer() - start))
    start = timeit.default_timer()
    main()
    print("Time: %s" % (timeit.default_timer() - start))
    start = timeit.default_timer()
    main()
    print("Time: %s" % (timeit.default_timer() - start))
