- [ ] **Todo** (initial state)
- [>] **In Progress** (update to this during work)
- [x] **Done** (mark complete with notes if needed)


# todo


# done

- [x] I want to instantiate a `Config` from a flat dictionary and
      access its values via dot notation (e.g., `cfg.host`), so that I
      can read configuration without bracket‑indexing and get
      immediate value from the package.
- [x] I want nested dictionaries to be automatically converted to
      recursive `Config` objects, so that I can access deeply nested
      values with dot notation (e.g., `cfg.database.host`) without
      manual wrapping.
- [x] I want to load config from a JSON file (via file path or
      file‑like object), so that I can use a standard,
      widely‑supported config format instead of hardcoding
      dictionaries. *(Shortcut: YAML is still hardcoded/missing – will
      be done in Task 4)*
- [x] I want to load config from a YAML file (via file path or
      file‑like object), so that I can use a human‑readable format
      that supports comments and structured data. *(Dependency:
      `pyyaml`)*
- [x] I want dictionaries inside lists to also be converted to
      `Config` objects, so that I can access fields of list‑item
      configs with dot notation (e.g., `cfg.users[0].name`).
- [x] I want to access configuration keys that are not valid Python
      identifiers (e.g., `"some-key"`, `"123invalid"`) via
      `__getitem__` only, so that I can still retrieve values from
      external config sources with unusual key names.
- [x] I want a useful `__repr__` of the `Config` object (e.g.,
      `Config(name='test', host='localhost')`), so that I can quickly
      inspect the config in a debugger or log output. *(This can be
      refined later if needed)*
