#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define		module	flask-login
Summary:	Flask-Login provides user session management for Flask
Summary(pl.UTF-8):	Obsługa zarządzania sesją użytkownika w aplikacjach Flask
Name:		python-%{module}
# keep python2 compatible version (0.5.x) here
Version:	0.5.0
Release:	7
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/F/Flask-Login/Flask-Login-%{version}.tar.gz
# Source0-md5:	a2d94aa6ae935345ebc68eb3cbb5fccd
URL:		https://github.com/maxcountryman/flask-login/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-flask
BuildRequires:	python-semantic_version
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-flask
BuildRequires:	python3-semantic_version
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

%description -l pl.UTF-8
Obsługa zarządzania sesją użytkownika w aplikacjach Flask. Wtyczka
obsługuje najpopularniejsze przypadki użycia: logowanie, wylogowanie,
zapamiętywanie sesji użytkowników przez określony czas.

%package -n python3-%{module}
Summary:	Flask-Login provides user session management for Flask
Summary(pl.UTF-8):	Obsługa zarządzania sesją użytkownika w aplikacjach Flask
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

%description -n python3-%{module} -l pl.UTF-8
Obsługa zarządzania sesją użytkownika w aplikacjach Flask. Wtyczka
obsługuje najpopularniejsze przypadki użycia: logowanie, wylogowanie,
zapamiętywanie sesji użytkowników przez określony czas.

%package apidocs
Summary:	API documentation for Python Flask-Login module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Flask-Login
Group:		Documentation

%description apidocs
API documentation for Python Flask-Login module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Flask-Login.

%prep
%setup -q -n Flask-Login-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest test_login
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest test_login
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py_sitescriptdir}/flask_login
%{py_sitescriptdir}/Flask_Login-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py3_sitescriptdir}/flask_login
%{py3_sitescriptdir}/Flask_Login-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
