%global realname meck
%global upstream eproxus
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:		erlang-%{realname}
Version:        0.8.4
Release:        1
Summary:        A mocking library for Erlang
Group:          Development/Erlang
License:        ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-hamcrest
BuildRequires:  erlang-rebar
# FIXME - calls to unexported cover:compile_beam/2, cover:get_term/1,
# cover:write/2


%description
With meck you can easily mock modules in Erlang. Since meck is intended to be
used in testing, you can also perform some basic validations on the mocked
modules, such as making sure no function is called in a way it should not.


%prep
%setup -q -n %{realname}-%{version}


%build
%{rebar_compile}


%install
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin
install -m 644 ebin/meck.app ebin/*.beam %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin


#%check
#{rebar_eunit} -C test.config


%files
%license LICENSE
%doc README.md NOTICE
%{_erllibdir}/%{realname}-%{version}/



%changelog
* Fri May 06 2016 neoclust <neoclust> 0.8.4-4.mga6
+ Revision: 1009756
- Rebuild post boostrap
- imported package erlang-meck

